#1
def count_positive(numbers):
    return len([num for num in numbers if num > 0])
#2
add_if_positive = lambda x, y: x + y if x > 0 and y > 0 else "Invalid"
#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]
#4
def has_vowel(s):
    vowels = 'aeiouAEIOU'
    return any(char in vowels for char in s)

def combine_if_vowels(str1, str2):
    if has_vowel(str1) and has_vowel(str2):
        return str1 + str2
    return None
#5
def longest_string(strings):
    return max(strings, key=len) if strings else None
