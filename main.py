import os
import msvcrt

PATH = os.path.dirname(os.path.abspath(__file__))
MOVIE_PATH = os.path.join(PATH, 'xrmb-movies.txt')
SERIE_PATH = os.path.join(PATH, 'xrmb-tv.txt')

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

def search_movie():
    movie = input("Entrez le nom du film : ")
    quality = input("Entrez la qualité du film (appuyez sur Entrée pour ignorer) : ")
    movie_name = replace_dots([movie])

    with open(MOVIE_PATH) as f:
        for line in f:
            for name in movie_name:
                if name in line and (quality == "" or quality in line):
                    print(line)

def search_serie():
    serie_name = input("Entrez le nom de la serie : ")
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

def search():
    print("1. Film")
    print("2. Serie")
    choice = input("Entrez votre choix : ")

    if choice == "1":
        search_movie()
    elif choice == "2":
        search_serie()

if __name__ == "__main__":
    search()
    wait_for_escape()