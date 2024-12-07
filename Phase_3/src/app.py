import PySimpleGUI as sg
import pandas as pd
from database import initialize_database
from model_initializer import initialize_models, load_models
from mood_model import predict_mood
from similar_songs_model import suggest_playlist
from genre_model import predict_genre
from popularity_model import predict_popularity


print("Initializing database...")
initialize_database()
print("Database initialized.")

print("Initializing models...")
initialize_models()
popularity_model, genre_model = load_models()
print("Models initialized.")

songs_dataset_path = "../data/Song_Data_with_Genre_Mapping.csv"
songs_dataset = pd.read_csv(songs_dataset_path)
cached_songs = {song.lower(): song for song in songs_dataset['song_name']}

# GUI layout
layout = [
    [sg.Text("CSE587 Data Intensive Computing Project Phase 3", font=("Arial", 30, "bold"), justification="center", expand_x=True, pad=(0, (20, 10)), background_color="#708090")],
    [sg.Text("Made by Shubham Soni, Hazel Mahajan, and Poojan Kaneriya", font=("Arial", 16), justification="center", expand_x=True, pad=(0, (10, 20)), background_color="#708090")],
    [sg.Text("Enter the Song Name:", font=("Arial", 18), justification="center", expand_x=True, pad=(0, (10, 10)), background_color="#708090")],
    [
        sg.InputText(
            key="-SONG_NAME-", 
            size=(50, 1), 
            pad=(10, (10, 5)), 
            justification="center", 
            font=("Arial", 14),
            border_width=1
        )
    ],
    [sg.Text("* Song name must be same as in the dataset.", font=("Arial", 12, "italic"), text_color="white", justification="center", expand_x=True, pad=(0, (0, 20)), background_color="#708090")],
    [sg.Text("Select Options:", font=("Arial", 18), justification="center", expand_x=True, pad=(0, (10, 20)), background_color="#708090")],
    [
        sg.Column(
            [
                [
                    sg.Checkbox("Mood", key="-MOOD-", font=("Arial", 14), pad=(10, 20), background_color="#708090"),
                    sg.Checkbox("Similar Songs", key="-SIMILAR-", font=("Arial", 14), pad=(10, 20), background_color="#708090"),
                    sg.Checkbox("Genre", key="-GENRE-", font=("Arial", 14), pad=(10, 20), background_color="#708090"),
                    sg.Checkbox("Popularity", key="-POPULARITY-", font=("Arial", 14), pad=(10, 20), background_color="#708090")
                ]
            ],
            justification="center", element_justification="center", expand_x=True, background_color="#708090"
        )
    ],
    [
        sg.Column(
            [
                [
                    sg.Button("Predict", key="-PREDICT-", size=(12, 1), font=("Arial", 16), pad=(10, (10, 20)), border_width=1),
                    sg.Button("Exit", key="Exit", size=(12, 1), font=("Arial", 16), pad=(10, (10, 20)), border_width=1)
                ]
            ],
            justification="center", element_justification="center", expand_x=True, background_color="#708090"
        )
    ],
    [sg.Text("Prediction Output:", font=("Arial", 18, "bold"), justification="center", expand_x=True, pad=(0, (10, 20)), background_color="#708090")],
    [
        sg.Multiline(
            "Your prediction will appear here.",
            size=(80, 15),  
            key="-OUTPUT-",
            font=("Arial", 14),
            pad=(10, (10, 50)), 
            justification="left",
            border_width=1,
            autoscroll=True,
            disabled=True, 
            write_only=True
        )
    ]
]

# Create and run GUI
window = sg.Window(
    "CSE587 Project GUI",
    layout,
    resizable=True,
    finalize=True,
    background_color="#708090",
    element_justification="center"
)
window.maximize()


while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "-PREDICT-":
        song_name = values["-SONG_NAME-"].strip().lower()
        mood = values["-MOOD-"]
        similar = values["-SIMILAR-"]
        genre = values["-GENRE-"]
        popularity = values["-POPULARITY-"]

        
        if not song_name:
            window["-OUTPUT-"].update("Please enter a song name.")
            continue

        
        if not any([mood, similar, genre, popularity]):
            window["-OUTPUT-"].update("Please select at least one option.")
            continue

       
        if song_name not in cached_songs:
            window["-OUTPUT-"].update(f"Song '{song_name}' not found in the dataset.")
            continue

        
        result = ""

        if mood:
            result += predict_mood(song_name) + "\n\n"
        if similar:
            similar_songs = suggest_playlist(song_name)
            if isinstance(similar_songs, pd.DataFrame): 
                suggested_song_names = similar_songs['song_name'].tolist()
                result += "Suggested Songs:\n" + "\n".join(suggested_song_names) + "\n\n"
        if genre:
            result += predict_genre(song_name) + "\n\n"
        if popularity:
            result += predict_popularity(song_name, songs_dataset, popularity_model) + "\n\n"

        
        window["-OUTPUT-"].update(result.strip())

# Close the window
window.close()
