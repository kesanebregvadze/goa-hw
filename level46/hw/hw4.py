import random

def random_fruit():
    fruits = ["apple", "MAN", "CURRY", "IDK"]
    favorite_fruit = random.choice(fruits)
    print(f"Your favorite random fruit is: {favorite_fruit}")


random_fruit()