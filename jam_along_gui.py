import streamlit as st
import pandas as pd
from open_webpage_in_chrome import get_song_lyrics
# Sample DataFrame
# data = {
#     'Song Name': ['Purani Jeans', 'Dum Laga Dum Laga', 'Yaaron', 'Pal', 'Roobaroo'],
#     'Year': [1993, 2007, 1999, 1999, 2005],
#     'Album/Film': ['Mahi', 'Dil, Dosti, Etc', 'Pal', 'Pal', 'Rang De Basanti']
# }

# df = pd.DataFrame(data)
df = pd.read_csv('songs.csv')
# Streamlit App layout
st.title("Interactive Song Selection Table")

# Display DataFrame in table format
st.write("Select a song from the table below:")

# Show table
st.table(df)

# Create a selectbox to choose the song name
selected_song = st.selectbox("Choose a song", df['song_name'])

# Function to be called when a song is selected
def handle_selection(selected_song):
    row_data = df[df['song_name'] == selected_song].iloc[0]
    st.write(f"**You selected:** {selected_song}")
    st.write(f"category: {row_data['category']}")
    # st.write(f"Album/Film: {row_data['Album/Film']}")
    get_song_lyrics(selected_song)
# Display the information of the selected song
if selected_song:
    handle_selection(selected_song)