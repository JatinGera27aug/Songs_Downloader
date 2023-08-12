# for installing given modules, run below commands in terminal
# pip install pytube
# pip install BeautifulSoup
# pip install urllib

# while running the program, it can throw you an error with code 410 : gone
# so to tackle this, use the below listed commands in order
# 1) python -m pip install --upgrade pytube
# 2) python -m pip install git+https://github.com/pytube/pytube
# and don't forgot to run cmd as admin, otherwise the changes won't happen

import pytube
from pytube import YouTube
from pytube import Search
import os

import requests
from bs4 import BeautifulSoup
def scrape():

    playlist_link = input("enter playlist link from gaana site: ")

    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-best-of-sonu-nigam")
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-with-love-hardy-sandhu")

    #personal fav
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-kk-heartbreak-hits")
    
    #most iconic playlist
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-best-of-kishore-kumar")

    data = requests.get(playlist_link)
    data = BeautifulSoup(data.text, "html.parser")
    return data

list_of_songs=[]
page=scrape()

try:
    music = page.find_all('a', class_="_tra t_over _plyCr")
    for text in music:
        get_name = text.get_text()
        get_name_sliced = get_name[9:]  
        list_of_songs.append(get_name_sliced)
except:
    message = f"not found !"
    print(message)

print(list_of_songs)


list_of_artist = []
try:
    music_artist = page.find_all('a', class_="_link")
    for text in music_artist:
        get_name_artist = text.get_text()
        list_of_artist.append(get_name_artist)
        list_of_only_artist = list_of_artist[2:]
        
except:
    message = f"not found !"
    print(message)

list_of_artist_and_music = []
try:
    music_artist_and_name = page.find_all('span', class_="t_over")
    for text in music_artist_and_name:
        get_name_artist_and_music = text.get_text()
        list_of_artist_and_music.append(get_name_artist_and_music)
        
except:
    message = f"not found !"
    print(message)

#-------------------------------------------------------
# for premium tag
premium_tag = input("\n \nIf there is any 'premium' tag mentioned beside song name: \nPress Y for Yes \nPress any other key for No \n")

#for choosing between video and audio
option = input("\nIn which format you want to download the song: \n1 for VIDEO \n2 for AUDIO \n")

if option == '1':
    choice_video_format = input("enter 1 for 360p or 2 for 720p quality \n")
elif option == '2':
    choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")


#for destination of downloading file
print("\nEnter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

for i in range(0,len(list_of_artist_and_music),2):   
    if (premium_tag == 'Y') or (premium_tag == 'y') :
        music = list_of_artist_and_music[i][9:]
    else:
        music = list_of_artist_and_music[i]

    count=0
    for j in list_of_artist_and_music[i+1]:
        if j!=',':
            count+=1
        else:
            break
    
    artist = list_of_artist_and_music[i+1][0:count]

    song = music+' by '+artist
        
    
    s = Search(song)
    print(song)
    a=[]
    for i in s.results:
        a.append(i)
    b=str(a[0])

    print("--------------------------")


    ee = len(b)-1
    for j in range(len(b)):
        if b[j]=="=":
            k=j+1
    video_id=b[k:ee]

    final_str = "https://www.youtube.com/watch?v="+video_id

    yt = YouTube(final_str)

    print("the title of video is:")
    print(yt.title, "\n") 



    if option == '1':
        vid = yt.streams.filter(progressive=True)
        if choice_video_format == '1':
            vid[1].download(output_path=destination,filename=music+'.mp4')
        elif choice_video_format == '2':
            vid[2].download(output_path=destination,filename=music+'.mp4')  
        else:
            exit 
        print("downloaded successfully: ", song)

    elif option == '2':
        # choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")
        aud = yt.streams.filter(only_audio=True)
       
        if choice_audio_format == '1':
            aud[1].download(output_path=destination,filename=music+'.mp3') 
        elif choice_audio_format == '2':
            aud[1].download(output_path=destination,filename=music+'.mp4')       
        else:
            exit 

        print("downloaded successfully: ", song)
    else:
        exit
