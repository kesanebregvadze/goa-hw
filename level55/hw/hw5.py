# 2. 10 ელემენტიანი tuple და პირველი სამი ელემენტის გამოყოფა
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_three, *rest = numbers[:3], numbers[3:]
print("პირველი სამი:", first_three)
print("დანარჩენი:", rest)

# 3. ქათმის სახელებზე dictionary, სადაც ერთ-ერთი ელემენტი tuple იქნება
chickens = {
    "ქათმის სახელი1":"hey hey",
    "ქათმის სახელი2":"ქათამა",
    "ქათმის სახელი3":("მიმი", "კიკი")
}
print("ქათმები:", chickens)

# 4. dictionary-ში არსებულ tuple-ს მივწვდეთ და გამოვიტანოთ პირველი ელემენტი
yellow_chicken_tuple = chickens["ქათმის სახილია2"]
first_element = yellow_chicken_tuple[0]
print("ყვითელი ქათმის პირველი ელემენტი:", first_element)

# 5. დანარჩენი ელემენტების rest-ში მოთავსება
_, *rest = yellow_chicken_tuple
print("ყვითელი ქათმის დანარჩენი ელემენტები:", rest)