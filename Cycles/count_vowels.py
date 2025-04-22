def count_vowels(string):

    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

result = count_vowels("Hello World")
print(f"Количество гласных в строке 'Hello World': {result}")
