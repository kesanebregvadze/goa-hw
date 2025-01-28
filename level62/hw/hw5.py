# 5
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    num_a = int(a)
    num_b = int(b)
    
    result = num_a + num_b
    
    return str(result)