import pytube
import string
import random

class YoutubeDownloader():
    
    def download_videos(self,save_path,video_list):
        for link in video_list:
            print(link)
            try:
                yt = pytube.YouTube(link)
            except:
                print("Bağlantı Hatası")

            yt.title = "".join(random.choice(string.ascii_lowercase) for i in range(10))
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]

            try:
                stream.download(save_path)
            except:
                print("Hata Alındı")
            print('İndirme Tamamlandı')
                
