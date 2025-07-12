from flask import Flask, render_template, request
import pickle
import numpy as np
import requests
import os
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)
app.secret_key = "simran-book-secret"

def fetch_similar_books_from_google(book_name):
    query = f"{book_name} personal development motivation success"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&orderBy=newest&maxResults=10&key={GOOGLE_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        books = []
        seen_titles = set()

        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', '').strip()
            authors = volume_info.get('authors', ['Unknown'])
            image_links = volume_info.get('imageLinks')
            thumbnail = image_links.get('thumbnail') if image_links else "/static/images/cover-not-found.jpg"
            description = volume_info.get('description', 'No description available.')
            categories = volume_info.get('categories', ['N/A'])

            title_lower = title.lower()
            if title_lower in seen_titles:
                continue
            seen_titles.add(title_lower)

            books.append([title, authors[0], thumbnail, description, categories[0]])
            if len(books) == 5:
                break

        return books

    except Exception as e:
        print(f"Error fetching from Google Books: {e}")
        return []

def fetch_details_from_google(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={GOOGLE_API_KEY}&maxResults=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            volume_info = data['items'][0]['volumeInfo']
            description = volume_info.get('description', "Description not available 😔")
            categories = volume_info.get('categories', ["Genre not available"])
            if not description or not categories:
                description_fallback, genre_fallback = fetch_details_from_open_library(book_title)
                description = description or description_fallback
                genre = categories[0] if categories else genre_fallback
            else:
                genre = categories[0]
        else:
            description, genre = fetch_details_from_open_library(book_title)

        return description, genre

    except Exception as e:
        print(f"Google Books error: {e}")
        return fetch_details_from_open_library(book_title)

def fetch_details_from_open_library(title):
    try:
        query = title.replace(' ', '+')
        url = f"https://openlibrary.org/search.json?title={query}&limit=1"
        response = requests.get(url)
        data = response.json()

        if data['docs']:
            doc = data['docs'][0]
            olid = doc.get('key', '').replace('/works/', '')
            detail_url = f"https://openlibrary.org/works/{olid}.json"
            detail_response = requests.get(detail_url)
            detail_data = detail_response.json()

            description = detail_data.get('description', 'Description not available 😔')
            if isinstance(description, dict):
                description = description.get('value', 'Description not available 😔')

            genre = detail_data.get('subjects', ['Genre not available 😔'])
            return description, genre[0] if genre else 'Genre not available 😔'

        return "Description not available 😔", "Genre not available 😔"

    except Exception as e:
        print(f"Open Library error: {e}")
        return "Description not available 😔", "Genre not available 😔"

@app.route('/')
def index():
    book_names = list(popular_df['book_title'].values)
    authors = list(popular_df['book_author'].values)
    images = list(popular_df['image_url_m'].values)
    votes = list(popular_df['number_of_ratings'].values)
    ratings = list(popular_df['avg_rating'].values)
    genres = []

    for title in book_names:
        _, genre = fetch_details_from_google(title)
        genres.append(genre)

    return render_template('index.html',
                           book_name=book_names,
                           author=authors,
                           image=images,
                           votes=votes,
                           rating=ratings,
                           genre=genres)

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', data=[], message=None)

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input').strip().lower()
    matched_books = [title for title in pt.index if title.lower() == user_input]

    if matched_books:
        actual_title = matched_books[0]
        index = np.where(pt.index == actual_title)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            temp_df = books[books['book_title'] == pt.index[i[0]]]
            book_title = temp_df.drop_duplicates('book_title')['book_title'].values[0]
            author = temp_df.drop_duplicates('book_title')['book_author'].values[0]
            image = temp_df.drop_duplicates('book_title')['image_url_m'].values[0]
            description, genre = fetch_details_from_google(book_title)
            data.append([book_title, author, image, description, genre])

        return render_template('recommend.html', data=data, message=None)

    else:
        data = fetch_similar_books_from_google(user_input)
        return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
