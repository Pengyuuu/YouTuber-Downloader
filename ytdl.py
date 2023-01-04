from pytube import YouTube
from sys import argv
import datetime

# grab link from command line input
link = argv[1]

yt = YouTube(link)

'''
m , s = divmod(yt.length, 60)
h, m = divmod(m, 60)
print(f'Downloading: {yt.title} {yt.publish_date} {h:d}:{m:02d}:{s:02d})
'''

print(f'Downloading: {yt.title} {yt.publish_date} {str(datetime.timedelta(seconds=yt.length))}')

yd = yt.streams.get_highest_resolution()

yd.download()