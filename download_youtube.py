from pytube import YouTube

url = YouTube('https://www.youtube.com/shorts/XVh4SO4fNT8')

hq_video = url.streams.get_highest_resolution()

hq_video.download()