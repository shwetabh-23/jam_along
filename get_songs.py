all_songs = '''1- Purani Jeans (1993)
Album- Mahi
Singer- Ali Haider
Music Directors- Jawahar Vattal, Faizi

2 - Dum Laga Dum Laga
Film- Dil, Dosti, Etc (2007)
Singers- Suraj Jagan, Hamza Faruqui, Sidarth- Suhas
Music Directors - Siddhartth, Suhash Kulkarni
Lyricist- Raam Goutam

3- Yaaron (1999)
Singer- KK
Album- Pal 
Lyricist- Mehboob

4- Pal (1999)
Singer- KK
Album- Pal 
Lyricist- Mehboob

5- Roobaroo (2005)
Film- Rang De Basanti 
Singers- A.R. Rahman, Naresh Iyer
Music Director- A.R. Rahman
Lyricist- Prasoon Joshi

6-  Aazadiyan (2010)
Film- Udaan
Singers- Amit Trivedi, Neuman Pinto & Amitabh Bhattacharya
Music Director- Amit Trivedi
Lyricist- Amitabh Bhattacharya

7-  Dil Dhadakne Do (2011)
Film- Zindagi Na Milegi Dobara 
Singer- Suraj Jagan, Joi Barua, Shankar Mahadevan 
Music Director- Shankar Ehsaan Loy
Lyrics- Javed Akhtar

8- Give Me Some Sunshine (2009)
Film- 3 Idiots
Singer- Suraj Jagan, Sharman Joshi
Lyricist- Swanand Kirkire
Music Director- Shantanu Moitra

9- Koi Kahe Kehta Rahe (2001)
Film- Dil Chahta Hai 
Singers- KK, Shaan, Shankar Mahadevan
Music Director- Shankar Ehsaan Loy
Lyricist- Javed Akhtar


10- Koi Mil Gaya (1998)
Film- Kuch Kuch Hota Hai 
Singers- Alka Yagnik, Udit Narayan, Kavita Krishnamurthy
Composers- Jatin - Lalit
Lyricist- Sameer

11 - Aaj Kal Zindagi (2009)
Film- Wake Up Sid 
Singer- Shankar Mahadevan
Music Directors- Shankar Ehsaan Loy
Lyricist- Javed Akhtar

12 - Aal Izz Well (2009)
Film- 3 Idiots
Singer- Sonu Nigam, Swanand Kirkire, Shaan
Music Director- Shantanu Moitra
Lyricist- Swanand Kirkire

13 - Jo Jeeta Wohi Sikandar  (1992)
Singer- Udit Narayan, Sadhana Sargam
Music Directors- Jatin-Lalit
Lyricist-  Majrooh Sultanpuri


14 - Rock On (2008)
Film Rock On!!
Singer- Farhan Akhtar
Music Directors- Shankar Mahadevan, Ehsaan Noorani, Loy Mendonca
Lyrics- Javed Akhtar

15- Behti Hawa Sa Tha Woh (2009)
Film- 3 Idiots
Singer- Shaan, Shantanu Moitra
Music Director- Shantanu Moitra
Lyricist- Swanand Kirkire

16 - Yaar Mod Do (2016)
Singer- Guru Randhawa ,Millind Gaba
Music Director- Millind Gaba
Lyrics- Guru Randhawa ,Millind Gaba'''
import re

def extract_song_names(songs_text):
    # Regular expression to find the song names
    # song_pattern = r"Song Name: ([^\n]+)"
    # # Extract all song names
    # song_names = re.findall(song_pattern, songs_text)

    song_pattern = r"\d+\s*-\s*([^\n]+)"
    # Extract all song names
    song_names = re.findall(song_pattern, songs_text)

    return song_names

songs = []
category = []

song_names = extract_song_names(all_songs)
for i, song in enumerate(song_names, start=1):
    songs.append(song)
    category.append('friendship songs')
    print(f"{i}. {song}")
# for i, song in enumerate(all_songs, start=1):
#     songs.append(song.split('-')[0].strip())
#     category.append('60 years of bollywood')
#     print(f"{i}. {song}")

import pandas as pd

data = pd.read_csv('songs.csv')
new_data = pd.DataFrame([songs, category]).T
new_data.columns = ['song_name', 'category']
data = pd.concat([data, new_data], ignore_index= True)
breakpoint()
# data.to_csv('songs.csv')
