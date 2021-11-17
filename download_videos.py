from ydownloader import YoutubeDownloader

downloader = YoutubeDownloader()

video_list = ["https://www.youtube.com/watch?v=vGm6rimkAZw","https://www.youtube.com/watch?v=IB3VVvF_2Iw","https://www.youtube.com/watch?v=vgoJW-G4KrQ"]

downloader.download_videos("youtube_videos",video_list)