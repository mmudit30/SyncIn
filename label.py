import cv2
import label_image, play_music_pygame
import sys, os, subprocess
from collections import Counter
from collections import defaultdict
size = 4

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
webcam = cv2.VideoCapture(0)

emotion_dict={'angry':'1', 'happy':'2', 'neutral or sad':'3'}
predictions = []


def calc_freq(L):
    most_common, num_most_common = Counter(L).most_common(1)[0]  # 4, 6 times
    return most_common

inf_loop=True
while inf_loop:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0)
    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))
    faces = classifier.detectMultiScale(mini)
    for f in faces:
        (x, y, w, h) = [v * size for v in f]
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        sub_face = im[y:y+h, x:x+w]
        FaceFileName = "test.jpg"
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)
        text = emotion_dict[text.title().lower()]
        predictions.append(text)
        if len(predictions)== 10:
            os.system('cls')
            print("\nDone")
            print(emotion_dict)
            print("predictions = ",predictions)
            predicted=calc_freq(predictions)
            print("predicted freq= ",predicted)
            predicted_str=list(emotion_dict.keys())[list(emotion_dict.values()).index(predicted)]
            print("I think you are ", predicted_str,"\n")
            play_music_pygame.main(predicted)
            inf_loop=False
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 1)
    cv2.imshow('Capture', im)
    key = cv2.waitKey(10)

    if key == 27: #The Esc key
        break
