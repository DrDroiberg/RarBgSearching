import os
import msvcrt
import tkinter
from tkinter import *

PATH = os.path.dirname(os.path.abspath(__file__))
MOVIE_PATH = os.path.join(PATH, 'xrmb-movies.txt')
SERIE_PATH = os.path.join(PATH, 'xrmb-tv.txt')

fenetre = Tk()
fenetre.geometry("750x250")

result_window = Tk()
result_window.geometry("750x250")

result_list = Listbox(result_window, width=100, height=100)

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

def get_value():
    value = entry.get()
    return value

def search_movie():
    movie = search_result
    # quality = input("Entrez la qualité du film (appuyez sur Entrée pour ignorer) : ")
    movie_name = replace_dots([movie])

    with open(MOVIE_PATH) as f:
        for line in f:
            for name in movie_name:
                if name in line: # and (quality == "" or quality in line):
                    print(line)

    # Create listbox with results
    result_list.insert(END, line)
    result_list.pack()

    result_window.mainloop()
def search_serie():
    serie_name = search_result
    season = input("Entrez la saison de la serie (appuyez sur Entrée pour ignorer) : ")
    episode = input("Entrez l'épisode de la serie (appuyez sur Entrée pour ignorer) : ")
    quality = input("Entrez la qualité du film (appuyez sur Entrée pour ignorer) : ")

    season = formatting_season(season)
    serie_name = replace_dots([serie_name])
    episode = formatting_episode(episode)

    with open(SERIE_PATH) as f:
        for line in f:
            for name in serie_name:
                if name in line and (quality == "" or quality in line) and (season == "" or season in line) and (episode == "" or episode in line):
                    print(line)

def search(movie_value, serie_value):
    # print("1. Film")
    # print("2. Serie")
    # choice = input("Entrez votre choix : ")

    if movie_value == 1:
        search_movie()
    if serie_value == 1:
        search_serie()

while True:
    # Search bar
    value = StringVar()
    value.set(" ")
    entry = Entry(fenetre, textvariable=value, width=50)
    entry.pack()

    search_result = entry.get()

    # Button movie and serie selection
    button_movie = Checkbutton(fenetre, text="Movie")
    button_movie.pack()

    movie_value = check_movie.get()
    print(movie_value)

    button_serie = Checkbutton(fenetre, text="Serie")
    button_serie.pack()

    serie_value = check_serie.get()
    print(serie_value)

    # Quality selection
    button_4k = Checkbutton(fenetre, text="4K")
    button_4k.pack()
    button_1080 = Checkbutton(fenetre, text="1080p")
    button_1080.pack()
    button_720 = Checkbutton(fenetre, text="720p")
    button_720.pack()

    quality_4k = check_quality_4k.get()
    quality_1080 = check_quality_1080.get()
    quality_720 = check_quality_720.get()

    # Button search
    search_button = Button(fenetre, text="Search", command=search(movie_value, serie_value))
    search_button.pack(side=tkinter.BOTTOM, padx=10)

    fenetre.mainloop()
# search()
# wait_for_escape()