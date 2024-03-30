import re
from urllib import error
from moviepy.editor import *
from pytube import Playlist
from yt_dlp import YoutubeDL, utils

class Downloader:

    def __init__(self, link_to_video="", link_to_playlist="", download_format="", folder_name=""):
        self.link_to_video = link_to_video
        self.link_to_playlist = link_to_playlist
        self.download_format = download_format
        self.folder_name = (self.sanitize_filename(folder_name) if folder_name else "Downloads")

    def sanitize_filename(self, filename):
        """Sanitize the file/folder names for avoiding OS errors"""

        sanitized_filename = re.sub(r'[\\/*?:"<>|\[\]]', "", filename)
        return sanitized_filename

    def sanitize_url(self, url):
        """Sanitize the URL to remove playlist parameters"""

        url_parts = url.split('&')
        for part in url_parts[:]:
            if 'list=' in part or 'index=' in part:
                url_parts.remove(part)

        sanitized_url = '&'.join(url_parts)
        return sanitized_url

    def fetch_videos_url(self):
        """Fetches the URLs of all videos in a YouTube playlist and returns a list containing the URL of each video"""

        if not self.link_to_playlist:
            return []
        playlist = Playlist(self.link_to_playlist)
        return playlist.video_urls
    
    def initialize_download(self, url):
        if self.download_format == "audio":
            self.download_audio_format(url)
        else:
            self.download_video_format(url)

    def download_videos(self):
        """Main function to fetch playlist links and download each video from its url"""

        if self.link_to_video:
            self.initialize_download(self.link_to_video)

        try:
            if self.link_to_playlist:
                video_urls = self.fetch_videos_url()

                if len(video_urls) == 0:
                    print("Playlist is empty")
                    print("NOTE: If your playlist is not empty and you still encounter this error message, most likely the playlist is private. Make it public and try again")
                    return

                for video_url in video_urls:
                    self.initialize_download(video_url)

        except KeyError:
            print("Wrong playlist URL entered! Enter the url in format youtube.com/playlist?list=[playlist_id]")

        except error.URLError:
            print(f"{self.link_to_playlist} is unreachable! Connect to internet")
            print("NOTE: If you are connected to internet and still getting this error message, then the playlist id might be wrong. Double check the url and try again")

        except Exception as e:
            print(f"Error extracting playlist URL : {e}")


    def download_audio_format(self, url):
        """Function to download in audio format"""

        url = self.sanitize_url(url)
        try:
            ydl_opts = {
                "format": "bestaudio/best", 
                "outtmpl": os.path.join(self.folder_name, "%(title)s.mp3"),
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except utils.DownloadError as e:
            print(f"{e}")

        except ValueError as e:
            print(f'{e}')

        except Exception as e:
            print(f"Error downloading audio from {url} : {e}")


    def download_video_format(self, url):
        """Function to download in video format"""

        url=self.sanitize_url(url)
        try:
            ydl_opts = {
                "format": "best",
                "outtmpl": os.path.join(self.folder_name, "%(title)s.%(ext)s"),
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except utils.DownloadError as e:
            print(f"{e}")

        except ValueError as e:
            print(f'{e}')

        except Exception as e:
            print(f"Error downloading video from {url} : {e}")

