from PIL import Image, ImageOps

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
        im=ImageOps.grayscale(im)
        im=resize_img(im,quality)
        arr=[]
        w,h=im.size
        for i in range(w):
            for j in range(h):
                intensity=im.getpixel((i,j))
                assert isinstance(intensity, int)
                index=intensity*(len(chars)-1)//255
                if chars[index]==" ":
                    arr.append(" ")
                arr.append(chars[index]+"")
            arr.append("\n")
        image="".join(arr)
    # print(image)
    return image

# if __name__=="__main__":
#     to_ascii(image_path, quality, chars)
