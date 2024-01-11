from pytube import YouTube

link="https://youtu.be/fTFRMziG8Ww?si=tFrS1YAAnnILyf0A"
youtube_1=YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos=youtube_1.streams.all()  #For all formats
# videos=youtube_1.streams.filter(only_audio=True) #only audio
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("Enter : "))
videos[strm].download()
print('Download Successfull')