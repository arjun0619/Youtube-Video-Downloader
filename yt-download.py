from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def ytdwn(url,save):
    try:
        yt = YouTube(url)
        stream=yt.streams.filter(progressive=True,file_extension="mp4")
        highQuality=stream.get_highest_resolution()
        highQuality.download(output_path=save)

    except Exception as e:
        print(e)

def openFile():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Select folder : {folder}")
    return folder


if __name__ == "__main__":
    root=tk.Tk()
    root.withdraw()
    

    url=input("Enter the YouTube url : ")
    save= openFile()
    
    if save:
        print("Video Downloading....")        
        ytdwn(url,save)
    else:
        print("Invalid Location")
