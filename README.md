## Infotact_Project_01
### Developed a personalized book recommendation system that suggests similar books based on user input using both machine learning and real-time API data. 

### **--Dataset Used--**
:) **Source :** https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
<br>

:) **Content :**
The Book-Crossing dataset comprises 3 files.
<br>

**[1] Users :**
Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values.
<br>

**[2] Books :**
Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.
<br>

**[3] Ratings :**
Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.
<br>

### **--How It Works--**
####  **Phase 1: Dataset-Based Recommendation (Collaborative + Popularity)**
:) Top-rated books shown on homepage using vote count + average rating
<br>

#### **Phase 2: Hybrid Content-Based Recommendation**
:) User enters a book title
<br>
**If found in local dataset :** 
<br>
- Recommend 5 most similar books using cosine similarity on TF-IDF vectors
<br>
**If not found :**
<br>
- Fetch recommendations in real-time from Google Books API
<br>
- Show relevant info like book cover, author, description, genre

  
###  Dataset Exploration
:) Total unique task descriptions: 265
<br>
:) Total unique categories: 13
<br>
:) Total unique skills: 232
<br>

###  Skill Assignment to Users
:) A dictionary was created mapping 40 users to 3–4 random skills each
<br>

###  Deadline, Workload & Priority Assignment
:) **Deadline:** Random date within 60 days from today.
<br>

:) **Workload:** Random integer from 1 to 10.
<br>

:) **Priority Logic:**      
if days_left <= 7 or workload >= 8 → High  
elif days_left <= 20 → Medium  
else → Low
<br>

###  Task Assignment Based on Skills
:) Each task was assigned to a user who has the required skill. If no perfect match, a random user was assigned.
<br>

###  Text Preprocessing using NLP
Preprocessing on Task Description involved:
<br>
:) Lowercasing
<br>
:) Tokenizing
<br>
:) Removing stopwords & punctuation
<br>
:) Stemming
<br>

### Final Conclusion :
:) Cleaned Dataset Saved As: cleaned_dataset.csv
<br>
:) Download Triggered via: files.download('cleaned_dataset.csv')
<br>


## Step 2: Task Classification using NLP and ML
### **--Objective--**
To classify tasks into relevant categories using the task descriptions. Applied NLP preprocessing and trained two machine learning models – Naive Bayes and Support Vector Machine (SVM) – for multi-class classification.
<br>

### **--Key Steps--**
### Model Used :
:) Multinomial Naive Bayes
<br>
:) Linear Support Vector Classifier (SVM)
<br>

###  Dataset:
Used the cleaned dataset generated in step 1 which includes:
<br>
:) Processed_Description (preprocessed task text)
<br>
:) Category (target class)
<br>
:) Skill, Deadline, Priority, User Skills, and Assigned User columns
<br>

###  Results & Evaluation
**Naive Bayes:**
<br>
:) **Accuracy:** 94.30%
<br>
:) **Precision:** 94.20%
<br>
:) **Recall:** 94.30%
<br>

**Notable high scores in:**
<br>
:) Frontend, Documentation, Testing, Project Management – All achieved 95–100% accuracy
<br>
:) Slight drop in performance for rare categories like ui/ux design due to low support
<br>

**SVM:**
<br>
:) **Accuracy:** 95.57%
<br>
:) **Precision:** 95.90%
<br>
:) **Recall:** 95.57%
<br>

**Improved overall performance compared to Naive Bayes**
<br>
:) Consistently high performance across most classes
<br>
:) Handles imbalanced data better
<br>
:) Perfect scores in multiple categories including DevOps, Documentation, Project Management
<br>

### Final Conclusion :
Both models performed exceptionally well, but SVM slightly outperformed Naive Bayes in terms of accuracy and precision. It is more suitable for production-level task classification due to its better handling of class imbalance.


## Step 3: Priority Prediction & Recommended User Assignment
### **--Objective--**
In step 3, we focused on building a machine learning model to predict the priority of tasks based on multiple features and recommend the most suitable user for each task based on skills and workload. We experimented with Random Forest and XGBoost classifiers.
<br>

### **--Key Steps--**
### Data Preprocessing: :
:) Dropped rows with missing Priority values.
<br>
:) Encoded the Assigned User and Priority columns using LabelEncoder.
<br>
:) Calculated Days Left to the deadline using:
<br>
df['Days Left'] = (df['Deadline'] - pd.to_datetime('today')).dt.days.fillna(0)
<br>
:) Transformed User Skills into a numerical value using a simple heuristic: count of comma-separated skills.
<br>

###  Feature Set :
X = df[['User Skills', 'Workload', 'Assigned User Encoded', 'Days Left']]
<br>
y = df['Priority Encoded']
<br>

###  Train-Test Split :
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
<br>

###  **Random Forest Classifier :**
:) **Hyperparameter Tuning with GridSearchCV:**
<br>

param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
<br>

:) **Best Params:**
<br>
Best RF Params: {'max_depth': None, 'min_samples_split': 5, 'n_estimators': 100}
<br>

:) **Classification Report:**
![image](https://github.com/user-attachments/assets/f1b3a089-47ef-45a5-bfe3-8ed7ad94a144)
            
<br>

### **XGBoost Classifier:**
:) **Hyperparameter Tuning with GridSearchCV:**
<br>

xgb_param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, 10],
    'learning_rate': [0.01, 0.1, 0.2]
}
<br>

:) **Best Params:**
<br>
Best XGBoost Params: {'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 50}
<br>

:) **Classification Report:**
![image](https://github.com/user-attachments/assets/932c98f8-8209-4b1c-a567-11bf9205f47a)

<br>

### **Recommended User Assignment:**
Used a simple logic to assign tasks to users with matching skills and lowest workload:
<br>

def assign_task(task_row):
    eligible_users = df[df['User Skills'] == task_row['User Skills']]
    if not eligible_users.empty:
        return eligible_users.loc[eligible_users['Workload'].idxmin()]['Assigned User']
    return random.choice(df['Assigned User'].dropna().unique())
<br>

### **Final Output Sample:**
![image](https://github.com/user-attachments/assets/4b699157-d34a-4e5a-affd-d64d62c20ade)
<br>

## Step 4: Final Priority Prediction & Task Classification
### **--Objective--**
In step 4, we trained the final Random Forest model on the full dataset using the best hyperparameters found earlier, and classified tasks into types based on their skill requirements.
<br>

### **Approach:**
:) Trained the final Random Forest classifier with tuned parameters.
<br>
:) Created a simple function to categorize tasks into Task Types like Programming, Data Analysis, or General Task based on keywords in the User Skills.
<br>
:) Predicted task priorities and evaluated model performance.
<br>


###  Results:
**Random Forest Accuracy:** 1.00 (perfect accuracy on full dataset)
<br>
**Classification Report:**
<br>
![image](https://github.com/user-attachments/assets/5c11d3c6-1f16-4a83-9e52-3e45a0c365ac)
<br>


###  Visualizations:
:) Confusion matrix showing model predictions :
<br>
![image](https://github.com/user-attachments/assets/cbc95287-ed18-47a2-891b-b07e143693af)
<br>

:) Feature importance bar chart for key features
<br>
![image](https://github.com/user-attachments/assets/266462d0-f3a2-4333-8085-c1538a210a23)
<br>

:) Distribution plots for predicted priority levels and task types
<br>
![image](https://github.com/user-attachments/assets/c1b51f9a-75a2-4b18-a342-efefe2b3448f)
<br>
![image](https://github.com/user-attachments/assets/366e2b06-78d3-4532-91f9-cb5a63fa4775)
<br>


### Output:
The final summary table with predicted priorities and task types is saved as Final_Task_Summary.csv for further use.





























