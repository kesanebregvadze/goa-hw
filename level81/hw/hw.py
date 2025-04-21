# level 81: 
# 1)ავაგოთ კალკულატორი რომელსაც 3 პარამეტრი გადაეცემა a,b, opration 
# ამათი გამოყენებით უნდა გადაწყვიტოს opertaion თუ რა გაუკეთოს a, b -ს 
# მინიმუმ კალკულატორში უნდა იყოს:
# +
# -
# /
# //
# *
# **
# **ასევე დაწერეთ შემდეგი ფუნქციები:**
#1
def func(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '//': return a // b
    if op == '**': return a ** b
    return 'უცნობი ოპერაცია'

print(func(2, 3, '+'))   
print(func(2, 3, '**'))  


