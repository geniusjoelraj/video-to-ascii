from convert import convert
from render import render
from to_ascii import to_ascii
import os
import sys

video=sys.argv[1]
name=sys.argv[2]
dir="frames/"+name
ascii_dir="frames_ascii/"+name+"_ascii"
quality=100
speed=0.1
cached=False
n=0
recache=False

if not os.path.exists(dir): 
    os.makedirs(dir) 

if not os.path.exists(ascii_dir): 
    os.makedirs(ascii_dir) 
else:
    cached=True
    n=len(os.listdir(ascii_dir))


if not cached or recache:
    n=convert(video, dir)
    frame_files=["frame0"+str(i)+".jpg" for i in range(n)]
    frames=[dir+"/"+file for file in frame_files]

    for i in range(n):
        img=to_ascii(frames[i],quality)
        with open(ascii_dir+"/frame0"+str(i)+".txt", "w") as file:
            file.write(img)
try:
    render(ascii_dir, n, speed)
except KeyboardInterrupt:
    print("Stopped")
