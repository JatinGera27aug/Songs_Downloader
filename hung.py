import pytube
from pytube import YouTube
from pytube import Search


import requests
from bs4 import BeautifulSoup
def scrape():

    #playlist_link = input("enter playlist link from gaana site: ")
    
    #data = requests.get(f"https://www.jiosaavn.com/featured/best-of-2010s/gn19HTwL-lfgEhiRleA1SQ__")

    #this playlist se sbse jyada sikha, error handling + artist name ke saath search
    #data = requests.get(f"https://gaana.com/playlist/gaana-dj-best-of-sonu-nigam")

    data = requests.get(f"https://gaana.com/playlist/gaana-dj-kk-heartbreak-hits")

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



list_of_limited_songs = list_of_songs[2:9]


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

option = input("In which format you want to download the song: \n1 for VIDEO \n2 for AUDIO \n")


#for i in range(0,len(list_of_artist_and_music),2):
for i in range(0,10,2):
    music = list_of_artist_and_music[i][9:]
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
        aud = yt.streams.filter(only_audio=True)
        aud[1].download('~/DownloadsaudGAANA_KK_HEARTBREAK')
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