import time
import os


def render(dir,n,speed=0.1):
    frame_files=["frame0"+str(i)+".txt" for i in range(n)]
    frames=[open(dir+"/"+file).read() for file in frame_files]

    for i in range(100):
        for i in range(n):
            os.system('cls' if os.name == 'nt' else 'clear')
            # os.system('cat ./ascii-frames/frame0'+str(i)+'.txt')
            print(frames[i])

            i+=1
            time.sleep(speed)
