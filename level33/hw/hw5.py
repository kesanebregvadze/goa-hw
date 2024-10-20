# 5. შექმენით ცვლადი სახელად text და შეინახეთ ამ ცვლადში "i love html but its not a programming language :'(". შემდეგ წაშალეთ ამ ცვლადში ყველა სფეისი და დააბრუნეთ ტექსტი უკუღმა 
# (პროგრამამ უნდა დააბრუნოს "(':egaugnalgnimmargorpatonsti tublmthtaevoli")
text="i love html but its not a programming language :'("
text2=text.replace(" ","")
text3 = "".join(reversed(text2))
print(text3)