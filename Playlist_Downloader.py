from pytube import Playlist

py=Playlist("https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&si=6igxluzeKw-nWOoD")

print(f'Downloading : {py.title}')

for video in py.videos:
    print(f'Downloading : {video.title}')
    video.streams.first().download
    print("video downloaded")
    print()