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
    #data = requests.get(f"https://www.hungama.com/playlists/bollywood-top-40/6532/")

    #data = requests.get(f"https://www.hungama.com/playlists/todays-top-hindi/39100/")

    playlist_link = input("enter playlist or album link from hungama site: ")
    data = requests.get(playlist_link)
    
    data = BeautifulSoup(data.text, "html.parser")
    return data


page=scrape()

list_of_movies_or_album=[]
try:
    music = page.find_all('h5')
    for text in music:
        list_of_movies_or_album.append(text.get_text())
except:
    message = f"not found !"
    print(message)

list_of_songs=[]
try:
    music = page.find_all('h4')
    for text in music:
        song=text.get_text()
        song_name=song[1:]
        list_of_songs.append(song_name)
except:
    message = f"not found !"
    print(message)
print("songs name:")
print(list_of_songs)

#------------------------------------------
option = input("In which format you want to download the song: \n1 for VIDEO \n2 for AUDIO \n")
if option == '1':
    choice_video_format = input("enter 1 for 360p or 2 for 720p quality \n")
elif option=='2':
    choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")
else:
    exit

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'


list_final_songs=[]

for i in range(len(list_of_songs)):
    new_list_movie=list_of_movies_or_album[i].replace('(','').replace(')','').replace('"','').replace('.','')
    new_list_movies=new_list_movie.lower()

    new_list_songs = list_of_songs[i].lower()
    if new_list_songs[0]=='\n':
        song_name=new_list_songs[1:]
    else:
        song_name=new_list_songs
    len_word=len(list_of_songs[i])
    
    if new_list_songs==new_list_movies:
        list_final_songs.append(new_list_songs)

    elif new_list_songs[-5:] == 'From ':
        len_word=(len(new_list_songs)-5)
        if new_list_songs[0:len_word]==new_list_movies[:len_word]:
            list_final_songs.append(new_list_movies)

        else:
            bust = new_list_songs+''+new_list_movies
            list_final_songs.append(bust)

    elif new_list_songs[:-1]==new_list_movies[:len_word]:
        list_final_songs.append(new_list_movies)

    elif new_list_songs[:-1]!=new_list_movies:
        bust = new_list_songs+''+new_list_movies
        list_final_songs.append(bust)
        
    else:
        pass

print("\n -----------------------searching---------------\n")

for i in range(len(list_final_songs)):
    song=list_final_songs[i]
    print(song)
    s = Search(song)
    a=[]
    for m in s.results:
        a.append(m)
    b=str(a[0])

    print("--------------------------")

    ee = len(b)-1
    for j in range(len(b)):
        if b[j]=="=":
            k=j+1
    video_id=b[k:ee]  #video-id

    final_str = "https://www.youtube.com/watch?v="+video_id

    yt = YouTube(final_str)

    print("the title of video is:")
    print(yt.title,"\n") 

    if option == '1':
        vid = yt.streams.filter(progressive=True)
        if choice_video_format == '1':
            vid[1].download(output_path=destination,filename=song_name+'.mp4')
        elif choice_video_format == '2':
            vid[2].download(output_path=destination,filename=song_name+'.mp4')   
        else:
            exit 
        print("downloaded successfully: ", song)
    elif option == '2':
        aud = yt.streams.filter(only_audio=True)

        if choice_audio_format == '1':
            aud[1].download(output_path=destination,filename=song_name+'.mp3') 
        elif choice_audio_format == '2':
            aud[1].download(output_path=destination,filename=song_name+'.mp4') 
        else:
            exit 

        print("downloaded successfully: ", song)
    else:
        exit