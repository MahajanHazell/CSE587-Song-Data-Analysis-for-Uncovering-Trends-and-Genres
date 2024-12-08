import os
import pickle
from models.genre_model import train_genre_model
from models.popularity_model import train_popularity_model

# Paths to models and dataset
data_folder = "../data"
songs_dataset_path = os.path.join(data_folder, "Song_Data_with_Genre_Mapping.csv")
popularity_model_path = os.path.join(data_folder, "popularity_model.pkl")
genre_model_path = os.path.join(data_folder, "genre_model.pkl")

def initialize_models():
    """Train and save models if they don't exist."""
    # Popularity Model
    if not os.path.exists(popularity_model_path):
        print("Training popularity model...")
        train_popularity_model(songs_dataset_path, popularity_model_path)
        print("Popularity model trained and saved.")

    # Genre Model
    if not os.path.exists(genre_model_path):
        print("Training genre model...")
        train_genre_model(songs_dataset_path, genre_model_path)
        print("Genre model trained and saved.")

def load_models():
    """Load pre-trained models from .pkl files."""
    with open(popularity_model_path, "rb") as f:
        popularity_model = pickle.load(f)
    with open(genre_model_path, "rb") as f:
        genre_model = pickle.load(f)
    return popularity_model, genre_model
