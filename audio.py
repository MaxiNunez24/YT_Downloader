from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"

yt = YouTube(url, on_progress_callback=on_progress)
title = yt.title;
print(title)

ys = yt.streams.get_audio_only()
ys.download()



