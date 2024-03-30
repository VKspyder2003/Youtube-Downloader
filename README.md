# YouTube Video Downloader

A Python tool for downloading videos and playlists from YouTube in audio (mp3) or video (mp4) format.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/HalilDeniz/ICMPWatch.git
```

2. Navigate to the project directory:

```bash
cd YOUR_DIRECTORY
```


3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Make the **main.py** file executable:

```bash 
chmod +x main.py
```

5. Run the application:

```bash
./main.py -v -V https://www.youtube.com/watch?v=dQw4w9WgXcQpp -f "I just got Rickrolled"
```

## Usage

```bash
$ main.py --help
usage: main.py [-h] [-V VIDEO_LINK] [-P PLAYLIST_LINK] [-f FOLDER_NAME] (-a | -v)

Download your favourite YouTube videos/shorts in audio/video format

options:
  -h, --help            show this help message and exit
  -V VIDEO_LINK, --video VIDEO_LINK
                        Video link to download
  -P PLAYLIST_LINK, --playlist PLAYLIST_LINK
                        Playlist link to download
  -f FOLDER_NAME, --folder FOLDER_NAME
                        Specific folder name to save the downloaded songs (default is "Downloads")
  -a, --audio-format    Download videos in audio format
  -v, --video-format    Download videos in video format
```

## Arguments

- `--video`, `-V`: Specify the video/shorts link to download.
- `--playlist`, `-P`: Specify the playlist link to download a set of videos.
- `--folder`, `-f`: (Optional) Specify a custom folder name to store downloaded files (defaults to "Downloads").
- `--audio-format`, `-a`: Set the download format as audio.
- `--video-format`, `-v`: Set the download format as video.

## Examples

1. **Download a video in audio format:**
   ```bash
   python main.py -a -V https://www.youtube.com/watch?v=VIDEO_ID
   ```
2. **Download a video in video format:**
   ```bash
   python main.py -v -V https://www.youtube.com/watch?v=VIDEO_ID
   ```
3. **Download a playlist in audio format:**
   ```bash
   python main.py -a -P https://www.youtube.com/playlist?list=PLAYLIST_ID
   ```
4. **Download a playlist in video format:**
   ```bash
   python main.py -v -P https://www.youtube.com/playlist?list=PLAYLIST_ID
   ```
5. **Specify the folder name to store the downloaded files:**
   ```bash
    python main.py -V [video_link] -v -f "My Music"  
    python main.py -P [playlist_link] -a -f "My Audiobooks" 
   ```

### Note

1. You can download youtube shorts in the same way as mentioned above

2. If you encounter an error message in your terminal indicating that the ampersand (&) character is not allowed, consider enclosing the link within quotation marks to resolve the issue. For instance:
```bash
    python main.py -v -P "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D" -f "My Songs"
```

3. If your folder name contains spaces, try to enclose the folder name within quotation marks. For example "My Songs".




