# 3 შექმენით ფუნქცია, რომელიც სტრინგში დაამატებს შემთხვევით სიმბოლოებს (მაგ. #, *, %), რომლებსაც შორის დააკრავს რიცხვი 1-დან 10-მდე.
def rdnsymbl(text):
    smbl = ['#', '*', '%']
    smbl = smbl[0]
    nm = 5
    return f"{smbl}{nm}{smbl}{text}"

txt = "hi"
print(rdnsymbl(txt))
