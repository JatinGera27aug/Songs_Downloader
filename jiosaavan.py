# for installing given modules, run below commands in terminal
# pip install pytube
# pip install BeautifulSoup
# pip install urllib

# while running the below command, program can throw you an error with code 410 : gone
# so to tackle this, use the below listed commands in order
# 1) python -m pip install --upgrade pytube
# 2) python -m pip install git+https://github.com/pytube/pytube
# and don't forgot to run cmd as admin, otherwise the changes won't happen


import pytube
from pytube import YouTube
from pytube import Search


import requests
from bs4 import BeautifulSoup
def scrape():

    playlist_link = input("enter playlist link from jiosaavan site: ")
    
    # given below some playlists
    # https://www.jiosaavn.com/album/ek-villain/HR757XLeV10_

    # https://www.jiosaavn.com/album/jagga-jasoos/pMfyXKVqiaY_

    # https://www.jiosaavn.com/album/zid-original-motion-picture-soundtrack/xZZT9ec6oR0_

    data = requests.get(playlist_link)
    
    data = BeautifulSoup(data.text, "html.parser")
    return data

list_of_songs=[]
page=scrape()

try:
    music = page.find_all(class_="u-centi u-ellipsis u-color-js-gray u-margin-bottom-none@sm u-margin-right@sm u-margin-right-none@lg")
    for text in music:
        print(text.get_text())
        list_of_songs.append(text.get_text())
except:
    message = f"not found !"
    print(message)



print(list_of_songs)

#-------------------ARTISTS-------------------
list_of_artist = []
try:
    music_artist = page.find_all('p', class_="u-centi u-ellipsis u-color-js-gray u-margin-right@sm u-margin-right-none@lg")
    for text in music_artist:
        print(text.get_text())   
        get_name_artist = text.get_text()
        list_of_artist.append(get_name_artist)
        
except:
    message = f"not found !"
    print(message)

print("list of artist: \n", list_of_artist)
#-------------------------------------------------------

option = input("In which format you want to download the song: \n1 for VIDEO \n2 for AUDIO \n")
if option == '1':
    choice_video_format = input("enter 1 for 360p or 2 for 720p quality \n")
elif option=='2':
    choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")
else:
    exit

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'


for i in range(len(list_of_songs)):
    song=list_of_songs[i]+' by '+list_of_artist[i]
    only_artist = list_of_songs[i]  
    print(song)
    s = Search(song)
    a=[]
    print(len(s.results))
    for i in s.results:
        print(i)
        a.append(i)
    b=str(a[0])

    print(a)
    print("--------------------------")


    ee = len(b)-1
    print("length of b is:,", len(b))
    for j in range(len(b)):
        if b[j]=="=":
            k=j+1
            print(j)
    c=b[k:ee]

    final_str = "https://www.youtube.com/watch?v="+c

    print("this is c(rest):", c)

    print(final_str)
    yt = YouTube(final_str)

    print("the title of video is:")
    print(yt.title) 


    if option == '1':
        vid = yt.streams.filter(progressive=True)
        if choice_video_format == '1':
            vid[1].download(output_path=destination,filename=only_artist+'.mp4')
        elif choice_video_format == '2':
            vid[2].download(output_path=destination,filename=only_artist+'.mp4')   
        else:
            exit 
        print("downloaded successfully: ", song)
    elif option == '2':
        aud = yt.streams.filter(only_audio=True)

        if choice_audio_format == '1':
            aud[1].download(output_path=destination,filename=only_artist+'.mp3') 
        elif choice_audio_format == '2':
            aud[1].download(output_path=destination,filename=only_artist+'.mp4') 
        else:
            exit 

        print("downloaded successfully: ", song)
    else:
        exit