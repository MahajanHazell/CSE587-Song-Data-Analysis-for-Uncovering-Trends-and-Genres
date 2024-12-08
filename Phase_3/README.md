# CSE587-Song-Data-Analysis-for-Uncovering-Trends-and-Genres

Course Code: CSE587 Data Intensive Computing

Project Title: Song Data Analysis for Uncovering Trends and Genres

Team Members: 
Hazel Mahajan (50592568),
Shubham Soni (50593888), 
Poojan Kaneriya (50604221)

This repository consists of the Jupyter Notebook for the Data Intensive Computing course project.

About the project: By analyzing the dataset, this project aims to predict the genre and upcoming trends based on various attributes.

# PHASE 1

### File name : [50592568]__[50593888]__[50604221]_phase_1.ipynb

### File structure : 

1. TASK 1. - Forming the problem statement.


2. TASK 2. - Asking Questions.

  Questions asked by Hazel Mahajan (UBID - 50592568)
  Question 1: Is there an optimal song duration that correlates with higher popularity scores? Are shorter or longer songs generally more popular than those with average lengths in the dataset?
  Question 2: Do songs with higher danceability and energy scores have significantly higher popularity compared to songs with lower scores? How do these attributes individually and collectively influence the popularity of a song?

  Questions asked by Shubham Vikas Soni (UBID - 50593888)
  Question 3: Do specific music genres (such as pop, hip-hop, rock, etc.) consistently have higher average popularity scores compared to other genres in the dataset, and does the genre significantly impact a song's popularity?
  Question 4: How do audio features such as danceability, energy, and tempo correlate with the popularity of songs in the dataset? Which of these features has the strongest positive relationship with song popularity?

  Questions asked by Poojan Kaneriya(UBID - 50604221)
  Question 5: Do certain music genres, such as pop or rock, tend to feature songs with higher valence (happiness) scores? Is there a clear relationship between genre and the prevalence of upbeat, happy songs in the dataset?
  Question 6: Is there a negative correlation between acoustics and song popularity? Do songs with higher acoustics scores tend to be less popular than those with lower acoustic scores in the dataset?
  

3. TASK 3. -  Data Retrieval

   
4. TASK 4. - Data Cleaning


5. TASK 5. - Exploratory Data Analysis.

   EDA Done by Hazel Mahajan (UBID - 50592568)
   - Question 1 and its Hypothesis: The duration of a song (length in milliseconds) significantly affects its popularity.
   - EDA fot this hypothesis.
   - Analysis of EDA.
   - Question 2 and its Hypothesis: Songs with higher danceability and energy scores are more popular than songs with lower scores.
   - EDA fot this hypothesis.
   - Analysis of EDA.
  
   EDA Done by Shubham Soni (UBID - 50593888)
   - Question 3 and its Hypothesis: Certain genres are consistently more popular than others.
   - EDA fot this hypothesis.
   - Analysis of EDA.
   - Question 4 and its Hypothesis: Songs with higher danceability, energy, or tempo tend to have higher popularity ratings.
   - EDA fot this hypothesis.
   - Analysis of EDA.
  
   EDA Done by Poojan Kaneriya (UBID - 50604221)
   - Question 5 and its Hypothesis: Songs with higher acoustic ness scores are generally less popular.
   - EDA fot this hypothesis.
   - Analysis of EDA.
   - Question 6 and its Hypothesis: Different music genres tend to exhibit distinct characteristics in terms of valence (musical positivity) and danceability.
   - EDA fot this hypothesis.
   - Analysis of EDA.
   
# PHASE 2

### File name : [50592568]__[50593888]__[50604221]_phase_2.ipynb

### File structure : 

We continue Phase 2 after the completion of Phase 1 to maintain continuity.

1. Work done by Hazel Mahajan (UBID - 50592568)

 TASK - ALGORITHM 1 AND SUPPORTING VISUALISATIONS FOR QUESTION 1
- Algorithm used - Decission Tree (taught in class)
- Summary and Interpretation
- Visualisation
- EXPLANATION AND ANALYSIS FOR ALGORITHM 1

 TASK - ALGORITHM 2 AND SUPPORTING VISUALISATION FOR QUESTION 2
 
    
- Algorithm Used- SVM (not taught in class )
- Model Results and Interpretation
- TASK - EXPLANATION AND ANALYSIS FOR ALGORITHM 2


2. Work done by Poojan Kaneriya (UBID - 50604221)

 Hypothesis 1
- Algorithm used to validate the hypothesis: Random Forest Regression
- Explanation of Each Step
- Analysis of Results
- Conclusion

 Hypothesis 2
    
    
- Algorithm used to validate the hypothesis: k-Means
- Explanation of Each Step
- Analysis of Results
- Conclusion

3. Work done by Shubham Soni (UBID - 50593888)

 Hypothesis 1
- Algorithm used: Support Vector Regressor (SVR)
- Visualisation
- Explanation and Analysis

 Hypothesis 2
  
  
- Algorithm used: K-Means
- Visualisation
- Explanation and Analysis


# PHASE 3

### Folder name : [50592568]__[50593888]__[50604221]_phase_3

### Folder structure : 

Folder Structure:

```
DIC Project/
|-- app/
|   |-- src/
|   |   |-- app.py               # Main application orchestrator
|   |   |-- database.py          # Handles SQLite database initialization and operations
|   |   |-- model_initializer.py # Prepares and loads pre-trained models
|   |   |-- mood_model.py        # Logic for mood prediction
|   |   |-- similar_songs_model.py # Logic for similar songs recommendation
|   |   |-- genre_model.py       # Logic for genre prediction
|   |   |-- popularity_model.py  # Logic for popularity estimation
|   |   |-- train_model.py       # Script for training ML models (optional)
|   |-- data/
|   |   |-- Song_Data_with_Genre_Mapping.csv # Dataset file for song information
|   |   |-- mood_model.pkl       # Pre-trained model for mood prediction
|   |   |-- similar_songs_model.pkl # Pre-trained model for similar songs
|   |   |-- genre_model.pkl      # Pre-trained model for genre classification
|   |   |-- popularity_model.pkl # Pre-trained model for popularity estimation
|   |   |-- song_input.db        # SQLite database table for user inputs
|   |   |-- songs_data.db        # SQLite database table for song dataset
|-- exp/
|   |-- [50592568]__[50593888]_[50604221]_phase_2.ipynb # Phase 1 and 2 combine notebook
|-- DIC_PROJECT_REPORT.pdf   # Report 
|-- VideoRecording.mp4       # Demonstration of the app
|-- requirements.txt         # Lists dependencies required for the project
|-- README.md                # Documentation and usage instructions
```

Instructions to run the project:

- Prerequisites:

    Python 3.8+

- Required Python libraries:

    pandas
    
    numpy
    
    scikit-learn
    
    PySimpleGUI
    
    sqlite3

- Installation

    Clone the repository
    
    Install the dependencies: pip install -r requirements.txt
    
    Ensure the data/ folder contains the necessary dataset and pre-trained models.

- Run the Application:

    python src/app.py
    
    Using the GUI:
    
    Enter a song name in the input field.
    
    Select one or more prediction options (Mood, Similar Songs, Genre, Popularity).
    
    Click "Predict" to view the results.
    
    The predictions will appear in the output box below.


Some of the song names to try:

    - Smooth Criminal
    - Good Vibes
    - In The End
    - Hips Don't Lie
    - I Wish I Missed My Ex

  
