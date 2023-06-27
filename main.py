import os
import msvcrt

PATH = os.path.dirname(os.path.abspath(__file__))
MOVIE_PATH = os.path.join(PATH, 'xrmb-movies.txt')

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


def search_movie():
    movie = input("Entrez le nom du film : ")
    quality = input("Entrez la qualité du film (appuyez sur Entrée pour ignorer) : ")
    movie_name = replace_dots([movie])

    with open(MOVIE_PATH) as f:
        for line in f:
            for name in movie_name:
                if name in line and (quality == "" or quality in line):
                    print(line)

search_movie()



wait_for_escape()