import pytube
import string
import random


class YoutubeDownloader():
    # def __init__(self,save_path,video_list) -> None:
    #     self.save_path = save_path
    #     self.video_list = video_list
    
    def download_videos(self,save_path,video_list):
        # folder_path = "".join(random.choice(string.ascii_lowercase) for i in range(10))
        # save_path = os.path.join(save_path, folder_path)
        # os.makedirs(save_path)

        for link in video_list:
            print(link)
            try:
                # object creation using YouTube
                # which was imported in the beginning
                yt = pytube.YouTube(link)
            except:
                print("Connection Error") #to handle exception

            yt.title = "".join(random.choice(string.ascii_lowercase) for i in range(10))
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]

            try:
                # downloading the video
                stream.download(save_path)
            except:
                print("Some Error!")
            print('Task Completed!')
                
