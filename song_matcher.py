import csv
import streamlit as st
import math
from heapq import nsmallest
from genres_set import all_genres


def closest_songs(inputs):
    list_songs = []
    distance_list = []
    dist = 0

    with open("spotify_data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            song = []
            one_row = list(row)

            if one_row[6] == inputs[0]:
                list_songs.append(f"{one_row[2]} by {one_row[1]}")

                for i in [4, 7, 8, 12, 13, 14, 16, 17]:
                    song.append(float(one_row[i]))

                for i in range(8):
                    dist += (song[i] - inputs[i + 1]) ** 2
                dist = math.sqrt(dist)
                distance_list.append(dist)

        smallest = nsmallest(10, distance_list)
        bests = []
        for i in range(10):
            bests.append(list_songs[distance_list.index(smallest[i])])
        return bests


st.set_page_config(page_title="Song Matcher")
st.title("Which Song Is Right For You?")
st.write(
    "Pick values for the following attibutes and click the button to get your ideal song!"
)


genre = st.selectbox("Genre:", options=all_genres).lower()
popularity = int(st.slider("Popularity Level:", 0, 100, 50))
danceability = int(st.slider("Danceability:", 0, 100, 50))
energy = int(st.slider("Energy:", 0, 100, 50))
speechiness = int(st.slider("Speeechiness:", 0, 100, 50))
acouticness = int(st.slider("Acouticness:", 0, 100, 50))
instrumentalness = int(st.slider("Instrumentalness:", 0, 100, 50))
valence = int(st.slider("Valence:", 0, 100, 50))
tempo = st.slider("Tempo:", 0, 250, 125)

if st.button("Calculate!"):
    inputs = []
    inputs.extend(
        [
            genre,
            popularity,
            danceability / 100,
            energy / 100,
            speechiness / 100,
            acouticness / 100,
            instrumentalness / 100,
            valence / 100,
            tempo,
        ]
    )
    songs = closest_songs(inputs)
    st.subheader("The ten songs you'll likely enjoy the most are as follows:")

    for i in range(10):
        st.write(songs[i])
