#change counter and num_samples variable to your assigned range
#run the code in terminal using command 'python3 data.py'
#when program is running, hit the letter you want to train and when your hand is positioned, hit 0 
#when 200 photos are taken, it will finish 
#if you want to retake the photos for a letter, you must delete the original folder
# hit . to close program


import cv2
import os
import sys
cam = cv2.VideoCapture(0)
start = False
counter = 0
num_samples = 200
IMG_SAVE_PATH = 'images'
try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    if not ret:
        print("failed to grab frame")
        break
    if counter == num_samples:
       break
    #cv2.rectangle(frame, (910, 300), (1210, 600), (0, 0, 0), 2) #right side
    cv2.rectangle(frame, (10, 300), (310, 600), (0, 0, 0), 2) #left side
    k = cv2.waitKey(1)
    if k == ord('a'):
            name = 'a'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('b'):
            name = 'b'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('c'):
            name = 'c'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('d'):
            name = 'd'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('e'):
            name = 'e'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('f'):
            name = 'f'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('g'):
            name = 'g'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('h'):
            name = 'h'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('i'):
            name = 'i'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('j'):
            name = 'j'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('k'):
            name = 'k'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('l'):
            name = 'l'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('m'):
            name = 'm'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('n'):
            name = 'n'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('o'):
            name = 'o'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('p'):
            name = 'p'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('q'):
            name = 'q'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('r'):
            name = 'r'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('s'):
            name = 's'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('t'):
            name = 't'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('u'):
            name = 'u'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('v'):
            name = 'v'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('w'):
            name = 'w'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('x'):
            name = 'x'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('y'):
            name = 'y'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('z'):
            name = 'z'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if k == ord('1'):
            name = 'nothing'
            IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, name)
            os.mkdir(IMG_CLASS_PATH)
    if start:
        #roi = frame[300:600, 910:1210] #right
        roi = frame[300:600, 10:310] #left
        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(counter + 1))
        print(save_path)
        cv2.imwrite(save_path, roi)
        counter += 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"Collecting {}".format(counter),
            (710, 100), font, 2.0, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)
    if k == ord('0'):
        start = not start
    if k == ord('.'):
            break
print("\n{} image(s) saved to {}".format(counter, IMG_CLASS_PATH))
cam.release()
cv2.destroyAllWindows()

