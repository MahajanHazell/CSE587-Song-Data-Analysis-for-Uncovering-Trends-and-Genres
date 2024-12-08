import pickle
import pandas as pd

# Load the pre-trained model and label encoder
with open('../data/ml_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('../data/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Load the songs dataset for matching song features
songs_dataset = pd.read_csv('../data/Song_Data_with_Genre_Mapping.csv')

def predict_mood(song_name):
    """
    Predict the mood of a song by its name.
    :param song_name: The name of the song to predict the mood for.
    :return: Predicted mood or an error message.
    """
    # Retrieve song features by matching the song name
    song = songs_dataset[songs_dataset['song_name'].str.lower() == song_name.lower()]

    if song.empty:
        return f"Song '{song_name}' not found in the dataset."

    # Extract features for prediction
    features = song[['acousticness', 'danceability', 'energy', 'instrumentalness',
                     'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']]

    # Predict the mood
    predicted_encoded = model.predict(features)
    predicted_mood = label_encoder.inverse_transform(predicted_encoded)

    return f"The predicted mood for '{song_name}' is: {predicted_mood[0]}"
