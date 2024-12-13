# 2) შექმმენით ფუცნია სადაც იქენბა სია თქვნს საყავრელ ფილმებზე და random.choces() გამოყენებით დაამტეთ 4 რემდონ ფილმი
import random

def random_movies():
    movies = ["Inception", "The Dark Knight", "Titanic", "The Matrix", "Interstellar", "The Godfather"]
    random_movies = random.sample(movies, 4)
    print("Your random 4 movies are:")
    for movie in random_movies:
        print(movie)


random_movies()
