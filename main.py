import os
import msvcrt
import tkinter
from tkinter import *

PATH = os.path.dirname(os.path.abspath(__file__))
MOVIE_PATH = os.path.join(PATH, 'xrmb-movies.txt')
SERIE_PATH = os.path.join(PATH, 'xrmb-tv.txt')

fenetre = Tk()
fenetre.geometry("750x250")

check_movie = tkinter.IntVar()
check_serie = tkinter.IntVar()

check_quality_4k = tkinter.IntVar()
check_quality_1080 = tkinter.IntVar()
check_quality_720 = tkinter.IntVar()

def wait_for_escape():
    print("Appuyez sur la touche Echap pour quitter...")
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':  # Vérifie si la touche Echap est enfoncée
            break
# test
def replace_dots(movie_names):
    for i in range(len(movie_names)):
        movie_names[i] = movie_names[i].replace(' ', '.')

    return movie_names

def formatting_season(season):
    if len(season) == 1:
        season = "S0" + season
    elif len(season) == 2:
        season = "S" + season

    return season

def formatting_episode(episode):
    if len(episode) == 1:
        episode = "E0" + episode
    elif len(episode) == 2:
        episode = "E" + episode

    return episode

def quality():
    quality = [check_quality_4k.get(),
                     check_quality_1080.get(),
                     check_quality_720.get()]
    if(quality[0] == 1):
        quality[0] = "2160p"
    else:
        quality[0] = ""
    if(quality[1] == 1):
        quality[1] = "1080p"
    else:
        quality[1] = ""
    if(quality[2] == 1):
        quality[2] = "720p"
    else:
        quality[2] = ""

    return quality

def title_formating(movie):
    return movie

def search_movie():
    movie = entry.get()
    movie_name = replace_dots([movie])
    movie_quality = quality()

    # Créer une nouvelle fenêtre pour afficher les résultats
    result_window = Tk()
    result_window.geometry("750x250")
    result_list = Listbox(result_window, width=750, height=250)

    with open(MOVIE_PATH) as f:
        for line in f:
            for name in movie_name:
                if name in line and (movie_quality[0] == "" or movie_quality[0] in line) \
                        and (movie_quality[1] == "" or movie_quality[1] in line) \
                        and (movie_quality[2] == "" or movie_quality[2] in line):
                        result_list.insert(END, line.strip())

    # Create listbox with results
    result_list.insert(END, line)
    result_list.pack()

    result_window.mainloop()
def search_serie():
    serie_name = entry.get()
    serie_quality = quality()

    serie_name = replace_dots([serie_name])

    with open(SERIE_PATH) as f:
        for line in f:
            for name in serie_name:
                if name in line and (serie_quality[0] == "" or serie_quality[0] in line) and \
                        (serie_quality[1] == "" or serie_quality[1] in line) \
                        and (serie_quality[2] == "" or serie_quality[2] in line):
                    print(line)

def search():
    movie_value = check_movie.get()
    serie_value = check_serie.get()

    if movie_value == 1:
        search_movie()
    if serie_value == 1:
        search_serie()

while True:
    # Search bar
    value = StringVar()
    value.set("")
    entry = Entry(fenetre, textvariable=value, width=50)
    entry.pack()

    # Button movie and serie selection
    button_movie = Checkbutton(fenetre, text="Movie", variable=check_movie)
    button_movie.pack()

    button_serie = Checkbutton(fenetre, text="Serie", variable=check_serie)
    button_serie.pack()

    # Quality selection
    button_4k = Checkbutton(fenetre, text="4K", variable=check_quality_4k)
    button_4k.pack()
    button_1080 = Checkbutton(fenetre, text="1080p", variable=check_quality_1080)
    button_1080.pack()
    button_720 = Checkbutton(fenetre, text="720p", variable=check_quality_720)
    button_720.pack()

    # Button search
    search_button = Button(fenetre, text="Search", command=search)
    search_button.pack(side=tkinter.BOTTOM)

    fenetre.mainloop()
# search()
# wait_for_escape()