# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self, title = "Python", director = "Karolina", budget = 500):
        self.title = title
        self.director = director
        self.budget = budget


movie1 = Movie("HTML", "Lukas", 400)
print(movie1.title, movie1.director)




#movie1 = Movie("Python", "Karolina G.", 100)
#movie2 = Movie("JS", "Lukas", 10)
#movie3 = Movie("HTML", "Jonas", 30)

#print(movie1.title)

#movie2.budget = 500
print(movie2.budget)



