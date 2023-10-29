import youtube_dl
import re

def convert_video(video_url: str, directory: str):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )

    print(video_info)

    filename = f"{directory}/test_file.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__ == '__main__':
    convert_video('https://www.youtube.com/watch?v=krDWc30PAGg', 'test_videos')
