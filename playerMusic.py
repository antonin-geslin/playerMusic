from tkinter import *
from tkinter import ttk
import pygame
from pygame import mixer
import os
import random

fenetre = Tk()
fenetre.geometry("800x800")
fenetre.title("Deezer")
fenetre.resizable(FALSE,FALSE)
onglet = ttk.Notebook(fenetre)
onglet.config(width=800,height= 800)
onglet.pack()
frame1 = Frame(onglet, bg="#424242", width=800, height=800)
frame2 = Frame(onglet, bg="#424242", width=800, height=800)
frame1.pack(expand=1, fill=BOTH)
frame2.pack(expand=1, fill=BOTH)
onglet.add(frame1, text="Player")
onglet.add(frame2, text="Song")
frame_buttons = Frame(frame1,bg="#424242", width=800)
frame_buttons.pack()

print("Pour ajouter de nouvelles musiques téléchargez simplement le son de votre choix en .mp3 et ajoutez le dans le dossiers songs !!")
pygame.mixer.init()

def unpause():
        mixer.music.unpause()
        play_button.grid_forget()
        pause_button.grid(row=0, column=3, padx=30)

def pause():
    mixer.music.pause()
    pause_button.grid_forget()
    play_button.grid(row=0, column=3, padx=30)


def count_files():
    return len([f for f in os.listdir("songs")])

def files_titles(nb):
    song_title = [f for f in os.listdir("songs")]
    return song_title[nb]

def play_song(temp):
    song_title = [f for f in os.listdir("songs")]
    mixer.music.load(f"songs/{song_title[temp]}")
    if mixer.music.get_busy() == False:
        mixer.music.play()
    else:
        stop()
        mixer.music.play()
    title.config(text = song_title[temp])
    img_songs.config(image=imgs[temp])
    play_button.grid_forget()
    pause_button.grid(row=0, column=3, padx=30)

i = 0
while i < count_files():
    title = files_titles(i)
    temp = 0
    title_button = Button(frame2, text=title, font=("Arial", 15), command =lambda temp = i:play_song(temp),activebackground= "#424242", bg="#424242", borderwidth=0)
    title_button.grid(row = i , column=0)
    i += 1


def stop():
    mixer.music.stop()


def next_song():
    song = title.cget('text')
    titles = [f for f in os.listdir("songs")]
    j = 0
    while titles[j] != song:
        j+=1
    
    if j != count_files():
        play_song(j+1)

def prev_song():
    song = title.cget('text')
    titles = [f for f in os.listdir("songs")]
    j = 0
    while titles[j] != song:
        j+=1
    if j != 0:
        play_song(j-1)

def loop():
    if mixer.music.get_busy() == False:
        mixer.music.play(-1)
        loop_button.grid_forget()
        unloop_button.grid(row = 0, column = 0, padx = 20)
    else:
        stop()
        mixer.music.play(-1)
        loop_button.grid_forget()
        unloop_button.grid(row = 0, column = 0, padx = 20)

def unloop():
    stop()
    mixer.music.play(0)
    unloop_button.grid_forget()
    loop_button.grid(row = 0, column = 0, padx = 20)
    return

def random_music():
    return(random.randint(0, count_files()))


def volume_music(x):
    mixer.music.set_volume(float(x))

#images controleurs#
pause_button_image = PhotoImage(file="img/pause.png")
play_button_image = PhotoImage(file="img/play-buttton.png")
suiv_g = PhotoImage(file="img/suivant (1).png")
suiv_d = PhotoImage(file="img/suivant.png")
stop_image = PhotoImage(file="img/stop.png")
loop_image = PhotoImage(file="img/boucle.png")
unloop_image = PhotoImage(file="img/boucle.png")
aleatoire_image = PhotoImage(file="img/fleches-aleatoires.png")
#images controleurs#

#images sons#
img0 = PhotoImage(file="img_songs/img0.png")
img1 = PhotoImage(file="img_songs/img1.png")
img2 = PhotoImage(file="img_songs/img2.png")
img3 = PhotoImage(file="img_songs/img3.png")

imgs = [img0,img1, img2, img3]
#images sons#


#label et buttons#
title = Label(frame1, font=("Arial", 15), activebackground= "#424242", bg="#424242", borderwidth=0,)
title.pack(side = TOP, pady = 20)
img_songs = Label(frame1, width=500, height=500, activebackground= "#424242", bg="#424242", borderwidth=0,)
img_songs.pack(side = TOP, pady=50)
play_button = Button(frame_buttons, image=play_button_image, activebackground= "#424242", bg="#424242", borderwidth=0, command= unpause)
pause_button = Button(frame_buttons, image=pause_button_image, activebackground= "#424242", bg="#424242", borderwidth=0, command= pause)
suiv_g_button = Button(frame_buttons, image=suiv_g, activebackground= "#424242", bg="#424242", borderwidth=0, command=prev_song)
suiv_d_button = Button(frame_buttons, image=suiv_d, activebackground= "#424242", bg="#424242", borderwidth=0, command=next_song)
stop_button = Button(frame_buttons, image=stop_image, activebackground= "#424242", bg="#424242", borderwidth=0, command = stop)
loop_button = Button(frame_buttons, image=loop_image, activebackground= "#424242", bg="#424242", borderwidth=0, command = loop)
unloop_button = Button(frame_buttons, image=unloop_image, activebackground= "#424242", bg="#424242", borderwidth=0, command = unloop)
aleatoire_button = Button(frame_buttons, image=aleatoire_image, activebackground= "#424242", bg="#424242", borderwidth=0, command =lambda: play_song(random_music()))
volume_mixer = Scale(frame_buttons, from_= 1, to_= 0, resolution=0.1,  command =lambda x: volume_music(x))
volume_mixer.set(0.7)
#label et buttons#

#placements#
volume_mixer.grid(row = 0, column = 0, padx=20)
loop_button.grid(row = 0, column = 1, padx = 20)
suiv_g_button.grid(row = 0, column = 2)
play_button.grid(row = 0, column = 3 , padx = 30)
suiv_d_button.grid(row = 0, column = 4)
aleatoire_button.grid(row = 0, column = 5, padx = 20)
stop_button.grid(row = 0, column = 6)
frame_buttons.pack(side=BOTTOM,pady=20)
#placements#

fenetre.mainloop()

