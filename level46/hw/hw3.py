import random

def random_name():
    names = ["John", "Alice", "Bob", "Eve", "Charlie"]
    name_str = ""
    for i in range(5):
        name_str += random.choice(names) + " ❤️ "
    print(name_str)


random_name()