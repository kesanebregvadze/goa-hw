# 1) გზაზე მიდის კურდღელი, შემოხვდვდა მგელი უცებ, მგელს ქონდა სია კუდრღელბის 4 კურდღელი ეწერა სიაში, მგელმა უთხრა ამ კურდღეს შენ

# თუ ხარ ამ სიაში, მაგ შემთხვევაში, შეგჭამ!! 

# თუ არ ხარ საიში მაშინ გაგიშვებ,

# შევადგნითოთ ფუქნცია სადაც იქნება გადმოცემული სია, 4 ელემნტით შიგნთ უნდა ეწეროს სახლეები, თუ კურდღლის სახელი დამთვევა, სიაში არსებული კურდღების სახლებს მაგ შემთხვეში გამოგვიტანოს შედეგი  

# ოღონდ!! 

# უნდა გავნიხლიოთ ბევრი შემთხვევები

# def bunny_hunter( lst, bunny_name ):
def bunny_hunter(lst,bunny_name):
    if bunny_name == lst[0]:
        return "გაგიშვებ"
    elif bunny_name == lst[1]:
        return "გაგიშვებ"
    elif bunny_name == lst[2]:
        return "გაგიშვებ"
    elif bunny_name == lst[3]:
        return "გაგიშვებ"
    else:
        return "შეგჭამ!"
print(bunny_hunter(["lile","anna","kato","keso"],"keso"))
print(bunny_hunter(["lile","anna","kato","keso"],"annano"))
