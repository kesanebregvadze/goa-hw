
# 2) შემოაყვანინეთ მომხმარებელს ორი რიცხვი, თუ პირველი რიცხვი მეტია მეორეზე,დაპრინტეთ "პირველი რიცხვი მეტია მეორეზე", თუ მეორე რიცხვი მეტია პირველზე,დაპრინტეთ "მეორე 
# რიცხვი მეტია პირველზე", თუ რიცხვები ტოლია, დაპრინტეთ "რიცხვები არის ტოლი"

num = int(input("enter a number:"))
num2 =  int(input("enter a number:"))
if num < num2:
    print("მეორე რიცხვი მეტია პირველზე")
elif num > num2:
    print("პირველი რიცხვი მეტია მეორეზე")
else:
    print("რიცხვები არის ტოლი")