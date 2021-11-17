import cv2 
from modules.Face import FaceDetectionC,FaceMeshC
import sys
import glob
import os

def take_faces(data,detector,name):
    cap = cv2.VideoCapture(data)
    # size = int(cap.get(3)),int(cap.get(4))
    # result = cv2.VideoWriter(f'processed_videos/{name}', 
    #                      cv2.VideoWriter_fourcc(*'XVID'),
    #                      20, size)
    os.makedirs(f"faces/{name}")
    idx = 0
    while True:
        ret,img = cap.read()
        if ret == True:
            idx +=1
            img = detector.find(img,name,idx,draw=True)

            # cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
            # cv2.imshow("Image Frame",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    # result.release()
    
# Closes all the frames
cv2.destroyAllWindows()


detector = FaceDetectionC()
videos = glob.glob("youtube_videos\\*.mp4")
print(videos)


for video in videos:
    print(videos)
    name = video.split("\\")[-1].split(".")[0]
    print(name)
    take_faces(video,detector,name)

