# 2) 
# გყავს მოთამშე player რომელსაც სიცცოხლე ეს სიცოცხე არის intager

# შევამნათ 2 ფუქნცია სადაც ჩვენს player-ს 
# - 1) აემატება სისცოცოხლე increes_health()
# - 2) დააკლდება სიცოცხლე decress_health() 

# > tip: ფუქნციას მინუმუმ უნდა გადაეცეს 1 პარამეტრი ❤️

# ### **დავალება**:  შევმნათ ერთ იფუქნიცია main() სადაც გამოვიძახებთ ჩვენს ზემოთ შექმნილ ფუქნციევბს 
# საბოლოოდ კი დავპირინტავთ სიცოცხლის რაოდენობა
def increes_health(player):
    return player + 5
def decress_health(player):
    return player - 10
def func():
    print(decress_health(25))
    print(increes_health(30))
print(func())