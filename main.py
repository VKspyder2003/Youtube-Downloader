#!/usr/bin/env python

from downloader import Downloader
import argparse

parser = argparse.ArgumentParser(
    description='Download your favourite YouTube videos/shorts in audio/video format',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='''Example usage:
    
    # Download a video in audio format
    python main.py -a -V https://www.youtube.com/watch?v=VIDEO_ID
    
    # Download a video in video format
    python main.py -v -V https://www.youtube.com/watch?v=VIDEO_ID
    
    # Download a playlist in audio format
    python main.py -a -P https://www.youtube.com/playlist?list=PLAYLIST_ID
    
    # Download a playlist in video format
    python main.py -v -P https://www.youtube.com/playlist?list=PLAYLIST_ID

    # Specify the folder name to store the downloaded files
    python main.py -v -P https://www.youtube.com/playlist?list=PLAYLIST_ID -f "My Songs"\n\nNote:

    If you encounter an error message in your terminal indicating that the ampersand (&) character is not allowed, consider enclosing the link within quotation marks to resolve the issue.
    For example: python main.py -v -P "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D" -f "My Songs"
    ''',
)
parser.add_argument('-V', '--video', dest='video_link', help='Video link to download')
parser.add_argument('-P', '--playlist', dest='playlist_link', help='Playlist link to download')
parser.add_argument('-f', '--folder', dest='folder_name', help='Specific folder name to save the downloaded songs (default is "Downloads")', default='Downloads')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', '--audio-format', dest='audio_format', action='store_true', help='Download videos in audio format')
group.add_argument('-v', '--video-format', dest='video_format', action='store_true', help='Download videos in video format')


args = parser.parse_args()

video_link = args.video_link
playlist_link = args.playlist_link
folder_name = args.folder_name
download_audio = args.audio_format
download_video = args.video_format

download_format = 'audio' if download_audio else 'video'

if not video_link and not playlist_link:
    print('Please provide a video link or a playlist link')
else:
    downloader = Downloader(link_to_video=video_link, link_to_playlist=playlist_link, download_format=download_format, folder_name=folder_name)
    downloader.download_videos()
