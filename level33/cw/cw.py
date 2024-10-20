# # level 33:
# ```
# 1) შექმნით წინანდადება ,  f სტრინგით f"გამრჯობა ჩემი სახელი {}"  და შევინახოთ ცვლადში words
# 2) შექმნილი წინადადება გავხლლიჩოთ .split() და ეს შევიანხოთ splited_word ში (ცვლადში)
# 3) შეარეთე splited_word "".join() ფუნცქიციით
# ```
# 1.
name="kesane"
word= f"გამრჯობა ჩემი სახელი {name}"
print(word)
# 2.
splited_word= word.split(" ")
print(splited_word)
# 3.
print("გამარჯობა".join(splited_word))