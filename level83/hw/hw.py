# 1) გააკეთეთ 5 მაგალითი for loop-ზე და კარგად ახსენით კომენტარის სახით
name = "keso"
for i in range(5):  #ეს კოდი keso-ს დაპრინტავს ხუთჯერ.
    print(name)
print("----------------------")
for i in name:
    print(i)   # ეს კოდი დაპრინტავს keso-ს ცალცალკე.
print("----------------------")
for i in range(1, 6):
    print(i)  # ყოველი ციკლის დროს i მიიღებს მნიშვნელობას 1-დან 5-მდე
print("----------------------")
for number in range(1, 11):
    if number % 2 == 0:  # თუ რიცხვი გაიყოფა 2-ზე დარჩენილის გარეშე, მაშინ ის პარია
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")
print("----------------------")
numbers = [550, 50, 30, 36, 5130]
total = 0
for num in numbers:
    total += num  # ყოველი ციკლის დროს num-ს ვუმატებთ total-ს
print(f"ჯამი: {total}")  # საბოლოოდ ვბეჭდავთ ჯამს
