def find_min(numbers):
    min_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number

    return min_number

result = find_min([3, 1, 4, 1, 5])
print(f"Минимальное число в списке [3, 1, 4, 1, 5]: {result}")
