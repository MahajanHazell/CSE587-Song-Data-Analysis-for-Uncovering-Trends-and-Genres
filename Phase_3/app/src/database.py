import sqlite3
import os

# Paths
data_folder = "../data"
songs_data_db_path = os.path.join(data_folder, "songs_data.db")


def initialize_database():
    """
    Initialize the database. Creates tables if they do not exist.
    """
    conn = sqlite3.connect(songs_data_db_path)
    cursor = conn.cursor()

    # Create songs_data table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_name TEXT NOT NULL,
            song_popularity INTEGER,
            genre TEXT,
            mood TEXT,
            features TEXT  -- JSON or serialized features for machine learning
        )
    ''')

    # Create song_input table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS song_input (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_name TEXT NOT NULL,
            prediction_option TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def insert_user_input(song_name, prediction_option):
    """
    Insert user input into the song_input table.
    :param song_name: The name of the song entered by the user.
    :param prediction_option: The prediction option(s) selected by the user.
    """
    conn = sqlite3.connect(songs_data_db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO song_input (song_name, prediction_option)
        VALUES (?, ?)
    ''', (song_name, prediction_option))
    conn.commit()
    conn.close()


def fetch_song_from_dataset(song_name):
    """
    Fetch a song from the songs_data table.
    :param song_name: The name of the song to search for.
    :return: The row from the table if found; None otherwise.
    """
    conn = sqlite3.connect(songs_data_db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM songs_data WHERE LOWER(song_name) = ?
    ''', (song_name.lower(),))
    song = cursor.fetchone()
    conn.close()
    return song
