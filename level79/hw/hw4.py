# 4) დაწერე ფუნქცია, რომელიც მიიღებს ტემპერატურას და დააბრუნებს შესაბამის ტექსტს:

# 30°C → "ცხელა"

# 20-30°C → "თბილა"

# 10-19°C → "ცოტა ცივა"

# <10°C → "ძალიან ცივა"
def func(gradusi):
    if gradusi == 30 :
        return "ცხელა"
    elif 20 <= gradusi <= 30 :
        return "თბილა"
    elif 10 <= gradusi <= 19 :
        return "თბილა"
    elif  gradusi < 10 :
        return" ძალიან ცივა"
print(func(23))