name=input("Enter your password:")
password="kesanegoa"
if name == password:
     print("right password")
else:
    while name != password:
        print("wrong password")
        name=input("Enter your password:")
        
    