
from string import digits
from faker import Faker 
fake = Faker('pl_PL')

"""
print(fake.sentence(nb_words=4))
print(fake.random_number(digits=2))
print(fake.year())
print(fake.word())
print(fake.random_int(min=0, max=20, step=1))
"""

#Klasy!!!!!!!!!!!!!!!!!!!!!!!!

class Movie:
    """
    Klasa filmy
    movie_type = "science fiction", "fantasy", "drama",
                "romance", "comedy", "zombie", "action",
                "historical", "horror", "war")

    """

    def __init__(self, title, publication_year, movie_type, categories, number_of_playes = 0):
        self.title = title
        self.publication_year = publication_year
        self.movie_type = movie_type
        self.number_of_playes = number_of_playes
        self.categories = categories

    def __str__(self):
        return f'Film: "{self.title} ({self.publication_year})".'
    
    def play(self, step = 1):
        self.number_of_playes += step

    


class TvSeries(Movie):
    """
    Klasa seriale

    """

    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number


    def __str__(self):
        return f'TVSeries: "{self.title} S{self.episode_number}E{self.season_number} ({self.publication_year})".'



#FUNKCJE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def create_movies_series(number_of: int) -> list:
    """"   
    number_of (integer) - from 1 to ....... -> number of movies and TVseries

    """
    movies_series = []
    
    for _ in range(number_of):
        movies_series.append(Movie(title=fake.sentence(nb_words=4),
                                publication_year=fake.year(),
                                movie_type=fake.word(),
                                number_of_playes=fake.random_number(),
                                categories=0
                                )
                            )
    
    for _ in range(number_of):
        movies_series.append(TvSeries(title=fake.sentence(nb_words=4),
                                publication_year=fake.year(),
                                movie_type=fake.word(),
                                number_of_playes=fake.random_number(),
                                episode_number=fake.random_number(digits=2),
                                season_number= fake.random_number(digits=2),
                                categories=1
                                )
                            )

    return movies_series


def get_movies(mylist: list):
    """
    wyszukuje tylko filmy
    Znacznik categories = 0 oznacza filmy

    """
    result_list = []

    for i in range(len(mylist)):
        if mylist[i].categories == 0:
            result_list.append(mylist[i])

    return result_list


def get_series(mylist: list):
    """
    wyszukuje tylko seriale
    Znacznik categories = 1 oznacza seriale

    """
    result_list = []

    for i in range(len(mylist)):
        if mylist[i].categories == 1:
            result_list.append(mylist[i])

    return result_list


def search(mylist: list, mytitle: str):
    """
    mylist - lista filmów i seriali \n
    mytitle - szukany tytuł

    """

    for i in range(len(mylist)):
        if mylist[i].title.find(mytitle) > 0:
            print(mylist[i])
        

def decorator(func):
    def wrapper(mylist):
        for _ in range(10):
            func(mylist)
    return wrapper



@decorator
def generate_views(mylist):
    """
    mylist - cała lista filmów i seriali

    """
    n = len(mylist)-1
    
    random_number = fake.random_int(0, n, 1)
    mylist[random_number].number_of_playes = fake.random_int(0, 100, 1)
    print(mylist[random_number])
    print(mylist[random_number].number_of_playes)


def top_titles(mylist: list, number: int = 3) -> list:
    """
    mylist -> cała lista filmów i seriali \n
    number -> wybrana ilość tytułów od góry

    """
    by_titles = sorted(mylist, key=lambda movie: movie.number_of_playes, reverse=True)
    result = []
    for i in range(number):
        result.append(by_titles[i])
    
    return result



#MAIN PROGRAM!!!!!!!!!!!!!!!!!!!!!!!!


print("\n")

all_list = create_movies_series(7)

print("all_list:")
for i in range(len(all_list)):
    print(all_list[i])

print("\n")

only_movies = get_movies(all_list)
print("only_movies:")
for i in range(len(only_movies)):
    print(only_movies[i])

print("\n")
print("only series:")
only_series = get_series(all_list)

for i in range(len(only_series)):
    print(only_series[i])

print("\n")


print("Szukane tytuły: ")
search(all_list, 'am')

print("\n")

print("Przypadkowy tytuł:")
generate_views(all_list)

print("\n")


print("Najpopularniejsze tytuły:")
ab = 4
for i in range(ab):
    print(top_titles(all_list, ab)[i])

print("\n")

