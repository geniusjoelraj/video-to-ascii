from ascii_video.convert import convert, get_fps
from ascii_video.render import render
from ascii_video.to_ascii import to_ascii
import os
import sys
import config

video=sys.argv[1]
name=video[:video.index('.')]
dir="frames/"+name
ascii_dir="frames_ascii/"+name+"_ascii"
cached=False
n=0
quality=config.quality
speed=config.speed
recache=config.recache
recache_ascii=config.recache_ascii
chars=config.chars

if not os.path.exists(ascii_dir): 
    os.makedirs(ascii_dir) 
if not os.path.exists(dir): 
    os.makedirs(dir) 
else:
    cached=True
    n=len(os.listdir(ascii_dir))


fps = 30
# if not cached or recache:
if not cached or recache:
    n=convert("videos/"+video, dir)


fps = get_fps("videos/"+video)
print("FPS: ",fps)

speed = 1 / fps 


frame_files = [f"frame{str(i).zfill(3)}.jpg" for i in range(n)]
frames=[dir+"/"+file for file in frame_files]

# if recache_ascii or not cached:
if recache_ascii or not cached:
    for i in range(n):
        img=to_ascii(frames[i],quality, chars=chars)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Converting to ascii.{(i%3)*'.'}\nFrame: {i}/{n}")
        with open(ascii_dir+"/frame"+str(i).zfill(3)+".txt", "w") as file:
            file.write(img)
try:
    render(ascii_dir, n, speed)
except KeyboardInterrupt:
    print("Stopped")
