import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
songs_dataset = pd.read_csv('../data/Song_Data_with_Genre_Mapping.csv')

# Preprocessing: Ensuring song names are unique
songs_dataset = songs_dataset.drop_duplicates(subset='song_name')

# Normalizing numeric features for similarity calculation
numeric_features = ['song_popularity', 'song_duration_ms', 'acousticness',
                    'danceability', 'energy', 'instrumentalness', 'key',
                    'liveness', 'loudness', 'audio_mode', 'speechiness',
                    'tempo', 'time_signature', 'audio_valence']
scaler = StandardScaler()
songs_dataset[numeric_features] = scaler.fit_transform(songs_dataset[numeric_features])

def suggest_playlist(song_name, n_suggestions=5):
    """
    Suggest a playlist of similar songs.
    :param song_name: Name of the song to find similar songs for.
    :param n_suggestions: Number of similar songs to return.
    :return: DataFrame of similar songs or an error message.
    """
   
    song = songs_dataset[songs_dataset['song_name'].str.lower() == song_name.lower()]
    if song.empty:
        return f"Song '{song_name}' not found in the dataset."

    # Calculate similarity
    song_features = song[numeric_features].iloc[0].values.reshape(1, -1)
    all_features = songs_dataset[numeric_features].values
    similarity_scores = cosine_similarity(song_features, all_features).flatten()

    # Rank songs by similarity
    songs_dataset['similarity_score'] = similarity_scores
    similar_songs = songs_dataset.sort_values(by='similarity_score', ascending=False)

    # Filter out the selected song and return top suggestions
    suggestions = similar_songs[similar_songs['song_name'].str.lower() != song_name.lower()]
    suggestions = suggestions[['song_name', 'genre', 'song_popularity']].head(n_suggestions)

    return suggestions
