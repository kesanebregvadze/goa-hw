# # 3. შექმენით სია 10 ნებისმიერი რიცხვით შემდეგ კი:
# ა) მოაშორეთ ამ სიიდან ყველაზე პატარა რიცხვი.
# ბ) დაამატეთ რიცხვი 100 სიის თავში და ბოლოში.
# გ) დაალაგეთ სია თანმიმდევრობით.
# დ) დაპრინტეთ ეს სია.
# ა)
num_lst=[1,6,4,3,8,19,4,3,2]
num=min(num_lst)
num_lst.remove(num)
# ბ)
num_lst.insert(0,100)
num_lst.append(100)
# გ)
num_lst.sort()
# დ)
print(num_lst)