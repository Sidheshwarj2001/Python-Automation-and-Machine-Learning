from pytube import YouTube
import sys

link = sys.argv[1]

yt = YouTube(link)

print("title : ",yt.title)

print("Views : ",yt.views)

yd = yt.streams.filter(res="360p")

yd.download()

