import cv2

def convert(video,dir):
    cam = cv2.VideoCapture(video)

    current_frame=0
    while True:
        ret,frame=cam.read()

        if ret:
            name = dir+'/frame0'+str(current_frame)+'.jpg'
            cv2.imwrite(name,frame)
            current_frame+=1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()
    return current_frame
