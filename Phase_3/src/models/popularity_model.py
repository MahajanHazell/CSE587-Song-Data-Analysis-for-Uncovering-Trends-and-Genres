import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def train_popularity_model(dataset_path, model_save_path):
    """
    Train the popularity prediction model and save it as a .pkl file.
    :param dataset_path: Path to the dataset CSV file.
    :param model_save_path: Path to save the trained model.
    """
    # Load dataset
    df = pd.read_csv(dataset_path)

    # Prepare features and target
    features = df[['acousticness', 'danceability', 'energy', 'instrumentalness',
                   'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']]
    target = df['song_popularity']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    with open(model_save_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Popularity model trained and saved to {model_save_path}")

def prepare_model(dataset_path):
    """
    Load the dataset and prepare the model.
    :param dataset_path: Path to the dataset CSV file.
    :return: Dataset and trained model.
    """
    # Load dataset
    df = pd.read_csv(dataset_path)

    # Load the trained model
    with open("../data/popularity_model.pkl", "rb") as f:
        model = pickle.load(f)

    return df, model

def predict_popularity(song_name, songs_dataset, model):
    """
    Predict the popularity of a song given its name.
    :param song_name: Name of the song.
    :param songs_dataset: The songs dataset.
    :param model: Trained popularity model.
    :return: Predicted popularity.
    """
    # Check if song exists in the dataset
    song = songs_dataset[songs_dataset['song_name'].str.lower() == song_name.lower()]

    if song.empty:
        return f"Song '{song_name}' not found in the dataset."

    # Extract features for prediction
    features = song[['acousticness', 'danceability', 'energy', 'instrumentalness',
                     'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']]

    # Predict popularity
    predicted_popularity = model.predict(features)[0]

    return f"The predicted popularity for '{song_name}' is: {predicted_popularity:.2f}"
