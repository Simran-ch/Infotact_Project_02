## Infotact_Project_01
### Developed a personalized book recommendation system that suggests similar books based on user input using both machine learning and real-time API data. 

### **--Dataset Used--**
:) **Source :** https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
<br>

:) **Content :**
The Book-Crossing dataset comprises 3 files.
<br>
- **Users :** Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values.
- **Books :** Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.
- **Ratings :** Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.
<br>

### **--Project Overview--**
This system allows users to:
- Get top 50 popular books (based on ratings & votes)
- Search for a book and get **collaborative-filtering based recommendations**
- If the book doesn't exist in dataset then it will fetch real-time similar books via **Google Books API**
- View book cover, title, author, description, and genre beautifully styled in cards

  
### **--How It Works--**
####  **Phase 1: Dataset-Based Recommendation (Collaborative + Popularity)**
:) Top-rated books shown on homepage using vote count + average rating
<br>

#### **Phase 2: Hybrid Content-Based Recommendation**
:) User enters a book title
<br>

**If found in local dataset :** 
<br>
(a) Recommend 5 most similar books using cosine similarity on TF-IDF vectors
<br>


**If not found :**
<br>
(a) Fetch recommendations in real-time from Google Books API
<br>
(b) Show relevant info like book cover, author, description, genre

  


---



---

## 📂 Dataset Used

**Source**: [Kaggle - Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

- `Books.csv`: Contains book titles, ISBNs, image URLs, etc.
- `Ratings.csv`: User ratings for books
- `Users.csv`: User demographics (age, location)

---

## 🧠 ML Techniques Implemented

### ✅ Popularity-Based Recommendation
- Based on number of ratings and average rating
- Displays Top 50 books

### ✅ Collaborative Filtering (Memory-Based)
- Used user-book matrix (pivot table)
- Cosine similarity to compute similar books
- Recommendation returns 4 similar books from dataset

### ❌ Content-Based Filtering (TF-IDF)
> Not implemented yet — enhancement planned for future  
> Description/genre-based matching using TF-IDF + cosine similarity can be added

---

## ⚙️ How It Works

1. User searches for a book
2. If found in dataset:
   - System fetches 4 similar books using cosine similarity
3. If not found:
   - Calls **Google Books API** to get live recommendations
4. Displays results with:
   - Book cover image (fallback used if missing)
   - Title, Author, Description (Read More toggle), Genre

---

## 🛠 Tech Stack

| Tool         | Use                            |
|--------------|---------------------------------|
| Python       | Core logic                     |
| Pandas       | Data manipulation              |
| Flask        | Backend Web Framework          |
| scikit-learn | Cosine Similarity              |
| Bootstrap 5  | Frontend styling               |
| Google Books API | Real-time recommendations  |

---

## 🖥️ How to Run Locally

### ✅ Requirements

```bash
pip install flask pandas scikit-learn requests




























