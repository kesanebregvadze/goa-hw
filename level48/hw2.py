import random
name_list=["ძაღლი","კატა","მამალი"]
def name_random(names):
    print(f"თქვენი საყვარელი ცხოველი არის: {random.choice(names)} ")
name_random(name_list)