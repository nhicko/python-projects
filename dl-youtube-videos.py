from pytube import YouTube
import sys


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    print("Download is completed successfully")


Download(sys.argv[1])
