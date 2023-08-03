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
import os

import requests
from bs4 import BeautifulSoup
def scrape():

    playlist_link = input("enter playlist link from gaana site: ")

    #this playlist se sbse jyada sikha, error handling + artist name ke saath search
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-best-of-sonu-nigam")
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-with-love-hardy-sandhu")

    #personal fav
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-kk-heartbreak-hits")
    
    #most iconic playlist     https://gaana.com/artist/yo-yo-honey-singh
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-best-of-kishore-kumar")

    data = requests.get(playlist_link)
    data = BeautifulSoup(data.text, "html.parser")
    return data

list_of_songs=[]
page=scrape()

try:
    music = page.find_all('a', class_="_tra t_over _plyCr")
    for text in music:
        print(text.get_text())
        get_name = text.get_text()
        get_name_sliced = get_name[9:]   #to remove premium word
        #print("sliced name is:",get_name_sliced)
        list_of_songs.append(get_name_sliced)
except:
    message = f"not found !"
    print(message)



print(list_of_songs)



list_of_limited_songs = list_of_songs[5:9]


list_of_artist = []
try:
    music_artist = page.find_all('a', class_="_link")
    for text in music_artist:
        print(text.get_text())
        get_name_artist = text.get_text()
        list_of_artist.append(get_name_artist)
        list_of_only_artist = list_of_artist[2:]
        
except:
    message = f"not found !"
    print(message)

print(list_of_only_artist)


list_of_artist_and_music = []
try:
    music_artist_and_name = page.find_all('span', class_="t_over")
    for text in music_artist_and_name:
        print(text.get_text())
        get_name_artist_and_music = text.get_text()
        list_of_artist_and_music.append(get_name_artist_and_music)
        #list_of_only_artist_and_music = list_of_artist_and_music[2:]
        
except:
    message = f"not found !"
    print(message)
print("combined-------------")
print(list_of_artist_and_music)
#-------------------------------------------------------
# for premium tag
premium_tag = input("If there is any 'premium' tag mentioned beside song name: \nPress Y for Yes \nPress any other key for No \n")

#for choosing between video and audio
option = input("In which format you want to download the song: \n1 for VIDEO \n2 for AUDIO \n")

if option=='2':
    choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")


#for i in range(0,len(list_of_artist_and_music),2):

#ye range mein 2 isliye kyuki gana site pe list mein music aur singers do consecutive strings mein aa rhe they
for i in range(0,len(list_of_artist_and_music),2):
    if (premium_tag == 'Y') or (premium_tag == 'y') :
        music = list_of_artist_and_music[i][9:]
    else:
        music = list_of_artist_and_music[i]
    print("music name is:", music)
    count=0
    for j in list_of_artist_and_music[i+1]:
        if j!=',':
            count+=1
        else:
            break
    
    artist = list_of_artist_and_music[i+1][0:count]
    print("artist name is:", artist)

    song = music+' by '+artist
        
    
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
        vid[1].download('~/DownloadsGaana')
        print("downloaded successfully: ", song)
    elif option == '2':
        # choice_audio_format = input("enter 1 for mp3 format, 2 for mp4 format \n")
        aud = yt.streams.filter(only_audio=True)

        # not being used for now but might be
        '''
        out = aud[1].download('~/DownloadsaudGAANA_kishore_kumar2')
        base, ext = os.path.splitext(out)
        new_file = base+'.mp3'
        os.rename(out, new_file)'''


        #aud[1].download('~/DownloadsaudGAANA_kishore_kumar2')     #it will download music file in .mp4 version but with no title edit
        if choice_audio_format == '1':
            aud[1].download('~/DownloadsaudGAANA_hardy_sandhu',filename=music+'.mp3') #with title same as song not yt video
        elif choice_audio_format == '2':
            aud[1].download('~/DownloadsaudGAANA_hardy_sandhu',filename=music+'.mp4')       
        else:
            exit 

        print("downloaded successfully: ", song)
    else:
        exit
    # vid = yt.streams.filter(progressive=True)
    # vid[1].download('~/Downloads')
    


    #print(s.results)











#below original code
#songs = ['bekhayali', 'rang sharbato ka', 'haan tu hain']

'''
for song in list_of_limited_songs:
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
        vid[1].download('~/DownloadsGaana')
        print("downloaded successfully: ", song)
    elif option == '2':
        aud = yt.streams.filter(only_audio=True)
        aud[1].download('~/DownloadsaudGAANA')
        print("downloaded successfully: ", song)
    else:
        exit
    # vid = yt.streams.filter(progressive=True)
    # vid[1].download('~/Downloads')
    


    #print(s.results)'''
