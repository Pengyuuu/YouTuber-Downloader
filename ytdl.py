from pytube import YouTube, Playlist
import requests
from sys import argv
import datetime

option = int(argv[1])

if (option == 1):

    # grab link from command line input
    link = argv[2]

    yt = YouTube(link)

    '''
    m , s = divmod(yt.length, 60)
    h, m = divmod(m, 60)
    print(f'Downloading: {yt.title} {yt.publish_date} {h:d}:{m:02d}:{s:02d})
    '''

    print(f'Downloading: {yt.title} {yt.publish_date} {str(datetime.timedelta(seconds=yt.length))}')

    yd = yt.streams.get_highest_resolution()

    yd.download()

elif (option == 2):

    # Playlist cannot be private
    p = Playlist(argv[2])

    print(f'Downloading: {p.title}')

    for videos in p.videos:

        print(f'Downloading: {videos.title} {videos.publish_date} {str(datetime.timedelta(seconds=videos.length))}')

        videos.streams.get_highest_resolution().download()

elif (option == 3):

    yt = YouTube(argv[2])

    url = yt.thumbnail_url

    img_data = requests.get(url).content

    with open(f'{yt.title} thumbnail', 'wb') as handler: 

        handler.write(img_data)

elif (option == 4):

    yt = YouTube(argv[2])

    captions = yt.captions['en'].generate_srt_captions()

    captions.download(f'{yt.title} en-sub')