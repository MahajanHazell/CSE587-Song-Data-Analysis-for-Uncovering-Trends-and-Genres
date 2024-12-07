import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
try:
    songs_dataset = pd.read_csv('../data/Song_Data_with_Genre_Mapping.csv')
except FileNotFoundError:
    raise FileNotFoundError("Dataset not found. Please ensure 'Song_Data_with_Genre_Mapping.csv' exists in the '../data' folder.")

# Preprocessing: Ensuring song names are unique
songs_dataset = songs_dataset.drop_duplicates(subset='song_name')

# Normalizing numeric features for similarity calculation
numeric_features = [
    'song_popularity', 'song_duration_ms', 'acousticness',
    'danceability', 'energy', 'instrumentalness', 'key',
    'liveness', 'loudness', 'audio_mode', 'speechiness',
    'tempo', 'time_signature', 'audio_valence'
]
scaler = StandardScaler()
try:
    songs_dataset[numeric_features] = scaler.fit_transform(songs_dataset[numeric_features])
except KeyError as e:
    raise KeyError(f"Missing required numeric features in the dataset: {e}")

def suggest_playlist(song_name, n_suggestions=5):
    """
    Suggest a playlist of similar songs.
    :param song_name: Name of the song to find similar songs for.
    :param n_suggestions: Number of similar songs to return.
    :return: DataFrame of similar songs or an error message as a string.
    """
    # Find the song in the dataset
    song = songs_dataset[songs_dataset['song_name'].str.lower() == song_name.lower()]
    if song.empty:
        return f"Song '{song_name}' not found in the dataset."

    
    song_features = song[numeric_features].iloc[0].values.reshape(1, -1)
    all_features = songs_dataset[numeric_features].values
    similarity_scores = cosine_similarity(song_features, all_features).flatten()

    
    songs_dataset['similarity_score'] = similarity_scores

    
    similar_songs = songs_dataset[songs_dataset['song_name'].str.lower() != song_name.lower()]
    similar_songs = similar_songs.sort_values(by='similarity_score', ascending=False)

    # Return top suggestions
    suggestions = similar_songs[['song_name', 'genre', 'song_popularity']].head(n_suggestions)

    if suggestions.empty:
        return "No similar songs found."
    return suggestions

# Example usage
if __name__ == "__main__":
    test_song = "Shape of You"  
    result = suggest_playlist(test_song)

    if isinstance(result, str):  # If an error message is returned
        print(result)
    else:  # If a DataFrame of songs is returned
        print("Suggested Songs:")
        print(result)
