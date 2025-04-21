def capitals(word):
    return [index for index, letter in enumerate(word) if letter.isupper()]

# Example usage:
print(capitals("HeLLoWoRld"))  # Output: [0, 2, 3, 6, 8]
