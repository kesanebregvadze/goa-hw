# # 1)გზაზე მიდის მელი და შეხვდება დათვს
# მელიას დათვი ეკითხება:
# შენ თაფლი გიყვარს?
# კი, მიყვარს!
# მაშინ თუ ჩემს თავსატეხს ამოხსნი, თაფლს გაჭმევ, თუ ვერ - აქედან გაეთრიე!
# ფუნქცია:
# დათვი მელიას სთხოვს, რომ გადასცეს 6 ციფრისგან შემდგარი სია და იპოვოს მასში მაქსიმალური და მინიმალური რიცხვი.
def find_max_min(numbers):
    if len(numbers) != 6:
        return "გთხოვ შეიყვანო ზუსტად 6 ციფრი!"
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    return f"მაქსიმალური: {max_num}, მინიმალური: {min_num}"

numbers = []

print("შეიყვანე 6 რიცხვი (თითო რიცხვი ახალი ხაზიდან):")
for i in range(6):
    num = int(input(f"{i+1}) "))
    numbers.append(num)

result = find_max_min(numbers)
print(result)