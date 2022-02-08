
from string import digits
from faker import Faker 
fake = Faker('pl_PL')

print(fake.sentence(nb_words=4))
print(fake.random_number(digits=2))
print(fake.year())
print(fake.word())


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





def create_movies_series( number_of: int = 6) -> list:
    """"   
    number_of_cards (integer) - from 1 to .......

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

    """
    result_list = []

    for i in range(len(mylist)):
        if mylist[i].categories == 0:
            result_list.append(mylist[i])

    return result_list


def get_series(mylist: list):
    """
    wyszukuje tylko filmy

    """
    result_list = []

    for i in range(len(mylist)):
        if mylist[i].categories == 1:
            result_list.append(mylist[i])

    return result_list





all_list = create_movies_series()

for i in range(len(all_list)):
    print(all_list[i])

print("\n")

only_movies = get_movies(all_list)

for i in range(len(only_movies)):
    print(only_movies[i])

print("\n")

only_series = get_series(all_list)

for i in range(len(only_series)):
    print(only_series[i])

print("\n")

