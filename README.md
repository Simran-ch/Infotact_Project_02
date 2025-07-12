## Infotact_Project_01
### Developed a personalized book recommendation system that suggests similar books based on user input using both machine learning and real-time API data. 


### **--Features--**
:) Search any book and get personalized recommendations.
<br>
:) Hybrid Recommendation Engine using:
* Dataset-based matching with cosine similarity
* Real-time fallback using Google Books API
<br>
:) Beautiful and responsive Flask web interface
<br>
:) Each recommended book includes:
<br>
* Book cover
<br>
* Author
<br>
* Description (toggle Read More)
<br>
* Genre
<br>
:) Fallback for missing covers
<br>


### **--Dataset Used--**
**Source :** https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
<br>
**--Content--**
<br>
The Book-Crossing dataset comprises 3 files :-
<br>
**Users :** Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values.
<br>
**Books :** Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.
<br>
**Ratings :** Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.
<br>

###  **--How It Works--**
**Phase 1: Dataset-Based Recommendation (Collaborative + Popularity)**
<br>
:) Top-rated books shown on homepage using vote count + average rating
<br>
**Phase 2: Hybrid Content-Based Recommendation**
<br>
:) User enters a book title
<br>
:) If found in local dataset:
<br>
* Recommend 5 most similar books using cosine similarity on TF-IDF vectors
<br>
:) If not found:
<br>
* Fetch recommendations in real-time from Google Books API
<br>
* Show relevant info like book cover, author, description, genre
<br>



















