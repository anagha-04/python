
class Movie:

    title: str

    director: str

    language: str

    year: int

    def __init__(self,title,director,language,year):

        self.title = title

        self.director = director

        self.language = language

        self.year = year

    def display_movie(self):

        print(self.title,self.director,self.language,self.year)

    def __str__(self):
        
        return self.title

movie_instance = Movie("thattathin marayathu","vineeth sreenivasan","malayalam",2012)

movie_instance.display_movie()

print(movie_instance)