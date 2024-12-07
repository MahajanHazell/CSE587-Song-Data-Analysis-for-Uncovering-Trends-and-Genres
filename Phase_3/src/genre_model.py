import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

def train_genre_model(dataset_path, model_save_path):
    """
    Train the genre prediction model and save it as a .pkl file.
    :param dataset_path: Path to the dataset CSV file.
    :param model_save_path: Path to save the trained model.
    """
    # Load dataset
    df = pd.read_csv(dataset_path)

    # Encode genres
    label_encoder = LabelEncoder()
    df['genre_encoded'] = label_encoder.fit_transform(df['genre'])

    # Prepare features and target
    features = df[['acousticness', 'danceability', 'energy', 'instrumentalness',
                   'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']]
    target = df['genre_encoded']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the model and label encoder
    with open(model_save_path, "wb") as f:
        pickle.dump((model, label_encoder), f)

    print(f"Genre model trained and saved to {model_save_path}")

def predict_genre(song_name):
    """
    Predict the genre of a song given its name.
    :param song_name: Name of the song.
    :return: Predicted genre.
    """
    with open("../data/genre_model.pkl", "rb") as f:
        model, label_encoder = pickle.load(f)

    # Mock example of features for the song 
    song_features = {
        "acousticness": 0.5,
        "danceability": 0.6,
        "energy": 0.7,
        "instrumentalness": 0.1,
        "liveness": 0.3,
        "loudness": -5.0,
        "speechiness": 0.05,
        "tempo": 120.0,
        "audio_valence": 0.7
    }

    # Convert features to a DataFrame
    features_df = pd.DataFrame([song_features])

    # Predict genre
    genre_encoded = model.predict(features_df)
    predicted_genre = label_encoder.inverse_transform(genre_encoded)

    return f"The predicted genre for '{song_name}' is: {predicted_genre[0]}"
