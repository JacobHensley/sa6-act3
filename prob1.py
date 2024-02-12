number = 365
number_str = str(number)

digit_sum = sum(list(map(lambda x: int(x), number_str)))
print(digit_sum)