# 1 შექმენით ფუნქცია, რომელიც სიის ელემენტებს დაამატებს შემთხვევითი რიცხვები 1-დან 50-მდე.
import random
list=[1,5,6,4,6,3]
def fun():
    for i in range(1,50,1):
        print(f"{random.choice(list)}")
        
fun()