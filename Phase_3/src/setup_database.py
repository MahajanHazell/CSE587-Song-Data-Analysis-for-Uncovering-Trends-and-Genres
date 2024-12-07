import sqlite3
import pandas as pd
import os

# Paths
data_folder = os.path.join("..", "data")
csv_file = os.path.join(data_folder, "Song_Data_with_Genre_Mapping.csv")
songs_data_db = os.path.join(data_folder, "songs_data.db")
song_input_db = os.path.join(data_folder, "song_input.db")


df = pd.read_csv(csv_file)

# Initialize songs_data.db
conn_songs_data = sqlite3.connect(songs_data_db)
cursor_songs_data = conn_songs_data.cursor()

# Create songs_data table
songs_data_table = '''
    CREATE TABLE IF NOT EXISTS songs_data (
        song_name TEXT,
        song_popularity INTEGER,
        song_duration_ms INTEGER,
        acousticness REAL,
        danceability REAL,
        energy REAL,
        instrumentalness REAL,
        key INTEGER,
        liveness REAL,
        loudness REAL,
        audio_mode INTEGER,
        speechiness REAL,
        tempo REAL,
        time_signature INTEGER,
        audio_valence REAL,
        genre TEXT
    );
'''
cursor_songs_data.execute(songs_data_table)

# Check if songs_data table is empty
cursor_songs_data.execute("SELECT COUNT(*) FROM songs_data;")
if cursor_songs_data.fetchone()[0] == 0:
    df.to_sql("songs_data", conn_songs_data, if_exists="append", index=False)
    print("songs_data table populated with dataset.")
else:
    print("songs_data table already contains data.")

conn_songs_data.commit()
conn_songs_data.close()

# Initialize song_input.db
conn_song_input = sqlite3.connect(song_input_db)
cursor_song_input = conn_song_input.cursor()

# Create songs_input table
songs_input_table = '''
    CREATE TABLE IF NOT EXISTS song_input (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        song_name TEXT NOT NULL,
        prediction_option TEXT NOT NULL
    );
'''
cursor_song_input.execute(songs_input_table)

print("Databases initialized successfully.")
conn_song_input.commit()
conn_song_input.close()
