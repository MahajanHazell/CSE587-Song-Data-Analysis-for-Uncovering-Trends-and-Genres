import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

# Path to your dataset (update this if needed)
file_path = "../data/Song_Data_with_Genre_Mapping.csv"  # Ensure this file exists

# Step 1: Load the dataset
songs_dataset = pd.read_csv(file_path)

# Step 2: Define Mood Categories
def categorize_mood(row):
    if row['audio_valence'] > 0.6 and row['danceability'] > 0.6:
        return "Happy"
    elif row['audio_valence'] < 0.4 and row['tempo'] < 100:
        return "Sad"
    elif row['energy'] > 0.7 and row['tempo'] > 120:
        return "Energetic"
    else:
        return "Calm"

songs_dataset['mood'] = songs_dataset.apply(categorize_mood, axis=1)

# Step 3: Encode the mood labels
label_encoder = LabelEncoder()
songs_dataset['mood_encoded'] = label_encoder.fit_transform(songs_dataset['mood'])

# Step 4: Prepare data for training
features = songs_dataset[['acousticness', 'danceability', 'energy', 'instrumentalness',
                          'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']]
target = songs_dataset['mood_encoded']

# Step 5: Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 6: Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Step 8: Save the trained model and label encoder
with open("../data/ml_model.pkl", "wb") as model_file:
    pickle.dump(rf_model, model_file)

with open("../data/label_encoder.pkl", "wb") as encoder_file:
    pickle.dump(label_encoder, encoder_file)

print("Model and label encoder have been saved successfully!")
