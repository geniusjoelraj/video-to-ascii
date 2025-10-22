from PIL import Image, ImageOps
from ascii_video import colors
import sys

def resize_img(img,quality):
    width, height=img.size
    aspect_ratio=width/height
    height=quality
    width=int(height*aspect_ratio)
    return img.resize((width, height))

def to_ascii(image_path, quality=50, chars="鬱森冊花代日三二一丶 "[::-1]):
    with Image.open(image_path) as im:
        im=im.rotate(90,expand=True)
        im=im.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
        im=resize_img(im,quality)
        color_im=im.copy()
        im=ImageOps.grayscale(im)
        arr=[]
        w,h=im.size
        for i in range(w):
            for j in range(h):
                intensity=im.getpixel((i,j))
                assert isinstance(intensity, int)
                index=intensity*(len(chars)-1)//255
                # color = colors.colors[min(index * len(colors.colors) // len(chars), len(colors.colors) - 1)]
                color = colors.rgb_to_ansi(color_im.getpixel((i,j)))
                if chars[index]==" ":
                    arr.append(" ")
                arr.append(color+chars[index])
            arr.append(colors.end+"\n")
        image="".join(arr)
    # print(image)
    return image

if __name__=="__main__":
    image_path=sys.argv[1]
    quality=int(sys.argv[2]) or 100
    chars="夢希雨光山はしこのいうっ "

    img=to_ascii(image_path, quality, chars)
    print(img)
