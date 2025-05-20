import cv2

def convert(video,dir):
    cam = cv2.VideoCapture(video)
    img=cv2.read("../videos/"+video)
    scale_percent=50
    width=int(img.shape[1] * scale_percent / 100)
    height=int(img.shape[0] * scale_percent / 100)
    dim=(width,height)
    current_frame=0
    while True:
        ret,frame=cam.read()
        frame=cv2.resize(frame, dim)
        if ret:
            name = dir+'/frame0'+str(current_frame)+'.jpg'
            cv2.imwrite(name,frame)
            current_frame+=1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()
    return current_frame
