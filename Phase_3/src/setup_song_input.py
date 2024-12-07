import sqlite3
import os

# Paths
data_folder = "../data"
song_input_db_path = os.path.join(data_folder, "song_input.db")


def setup_song_input_database():
    """
    Create the song_input database and table if not already present.
    """
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    conn = sqlite3.connect(song_input_db_path)
    cursor = conn.cursor()

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
    print(f"Database {song_input_db_path} initialized successfully.")


if __name__ == "__main__":
    setup_song_input_database()
