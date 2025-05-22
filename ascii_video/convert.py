import cv2
import os
import sys

def convert(video,dir):
    cam = cv2.VideoCapture(video)
    fps = cam.get(cv2.CAP_PROP_FPS)

    current_frame=0
    if not cam.isOpened():
        print("Cannot open video")
    while True:
        ret,frame=cam.read()

        if ret:
            name = dir + '/frame' + str(current_frame).zfill(3) + '.jpg'
            cv2.imwrite(name,frame)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"convering.{(current_frame%3)*'.'}\nFrame: {current_frame}/{int(cam.get(cv2.CAP_PROP_FRAME_COUNT))}")
            current_frame+=1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()
    return current_frame

def get_fps(video):
    cam = cv2.VideoCapture(video)
    fps = cam.get(cv2.CAP_PROP_FPS)
    return fps

if __name__=="__main__":
    convert(sys.argv[1], "misc")
