def fake_bin(s):
    return ''.join('0' if int(char) < 5 else '1' for char in s)


print(fake_bin("45385593107843568")) 
print(fake_bin("509321967506747"))