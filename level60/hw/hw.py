# 1
def number_to_string(num):
    return str(num)


    def number_to_string(num):
        return "%d" % num
        
            
        def number_to_string(num):
            return "{}".format(num)
            
            def number_to_string(num):
                return f"{num}"

# 2

def string_to_array(s):
    return s.split()


print(string_to_array("Robin Singh")) 
print(string_to_array("I love arrays they are my favorite")) 

# 3
def string_to_number(s):
    return int(s)

# 4
def fake_bin(x):
    result = ''
    for digit in x:
        if digit < '5':
            result += '0'
        else:
            result += '1'
    return result

# 5
def solution(string):
    return string[::-1]