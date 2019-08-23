import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard  # using module keyboard
import pygame
import pandas as pd
import random

def main(emotion_num):
    pygame.mixer.init()
    emotion_dict = {'1':'Angry', '2':'Happy', '3':'NeutralOrSad'}
    filename=emotion_dict[emotion_num]+".csv"
    df = pd.read_csv(filename)

    df_top = (df.columns)[0]
    count = df[df_top].count()
    random_index=random.randrange(0, count, 1)
    song_name = df[df_top][random_index]

    path='songs/'+song_name+'.mp3'

    pygame.mixer.music.load(path)
    print("Playing: ",song_name)
    print("Actions: ")
    print("\tP: pause")
    print("\tR: resume")
    print("\tS: Stop")
    print("\tE: exit")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed('p'):
            pygame.mixer.music.pause()
            os.system('cls')
            print("Playing: ", song_name)
            print("Paused")
            print("\tPress 'r' to resume")
            continue
        if keyboard.is_pressed('r'):
            pygame.mixer.music.unpause()
            os.system('cls')
            print("Playing: ", song_name)
            print("resumed")
            print("\tPress 'e' to exit")
            print("\tPress 's' to stop")
            print("\tPress 'p' to pause")
            continue
        if keyboard.is_pressed('s'):
            pygame.mixer.music.stop()
            print("You Pressed 'Stop' Key!")
            # print("\tNow song will play from starting")
            continue
        if keyboard.is_pressed('e'):
            print("You Pressed 'Exit' Key!")
            break  # finishing the loop
        continue
