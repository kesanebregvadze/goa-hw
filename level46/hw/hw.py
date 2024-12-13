# 1) შექემენით ფუცნია სადაც იქენბა სია ცხვოლებეზე და random.choces() გამოყენებით დაამატეთ ახალ საიში რენდომ ცოხველები
import random

def random_animal():
    animals = ["dog", "cat", "carrot", "snake", "monkey", "bear"]
    random_animal = random.choice(animals)
    print(f"New random animal: {random_animal}")


random_animal()
