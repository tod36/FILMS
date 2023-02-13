import os
import sys
import django
import pandas as pd
from movies.models import Film

# from manage import DJANGO_SETTINGS_MODULE

django.setup()

sys.path.append('/F/PYTHON 18 08 2020/2023/VERO/films/movies')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django.project.settings')


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)


def run():
    print('reading csv ...')
    film_df = pd.read_csv('movies/data/films.csv')
    film_array = film_df.to_dict(orient='records')
    for entry in film_array:
        film = Film(
            name=entry['title'],
            length=entry['length'],
            year=entry['year'],
            genre=entry['genre'],
        )
        film.save()
    print('Saved all entries to database')
    return


if __name__ == '__main__':
    # import django
    # django.setup()
    run()

# if __name__ == "__main__":
#     print("Hello, World!hhhhhhh")
