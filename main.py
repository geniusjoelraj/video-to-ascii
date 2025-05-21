from ascii_video.convert import convert
from ascii_video.render import render
from ascii_video.to_ascii import to_ascii
import os
import sys
import config

video=sys.argv[1]
name=sys.argv[2]
dir="frames/"+name
ascii_dir="frames_ascii/"+name+"_ascii"
cached=False
n=0
quality=config.quality
speed=config.speed
recache=config.recache
recache_ascii=config.recache_ascii

if not os.path.exists(ascii_dir): 
    os.makedirs(ascii_dir) 
if not os.path.exists(dir): 
    os.makedirs(dir) 
else:
    cached=True
    n=len(os.listdir(ascii_dir))


if not cached or recache:
    n=convert(video, dir)

frame_files=["frame0"+str(i)+".jpg" for i in range(n)]
frames=[dir+"/"+file for file in frame_files]

if recache_ascii:
    for i in range(n):
        img=to_ascii(frames[i],quality)
        with open(ascii_dir+"/frame0"+str(i)+".txt", "w") as file:
            file.write(img)
try:
    render(ascii_dir, n, speed)
except KeyboardInterrupt:
    print("Stopped")
