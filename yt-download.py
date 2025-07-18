from pytubefix import YouTube

def ytdwn(url):
    try:
        yt = YouTube(url)
        stream=yt.streams.filter(progressive=True,file_extension="mp4")
        highQuality=stream.get_highest_resolution()
        highQuality.download()
        print("The video downloaded")

    except Exception as e:
        print(e)
        print("An unexpected error occured")



url = input("Enter the URL of the video")
print("The video is downloading....")
ytdwn(url)

