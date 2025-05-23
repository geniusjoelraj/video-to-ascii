import time
import os


def render(dir,n,speed=0.1):
    frame_files = [f"frame{str(i).zfill(3)}.txt" for i in range(n)]
    frames=[open(dir+"/"+file).read() for file in frame_files]

    for i in range(1):
        for i in range(n):
            os.system('cls' if os.name == 'nt' else 'clear')
            # os.system('cat ./ascii-frames/frame0'+str(i)+'.txt')
            print(frames[i])
            time.sleep(speed)
