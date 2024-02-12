def find_maximum(numbers, comparison):
    maximum = numbers[0]
    
    for n in numbers:
        if comparison(n, maximum):
            maximum = n

    return maximum

numbers = [1, 2, 3, 4, 5, 6]
print(find_maximum(numbers, lambda x, y: x > y))