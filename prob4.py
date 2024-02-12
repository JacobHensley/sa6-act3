def intersection(list1, list2):
    result = list(filter(lambda x: x in list2, list1))
    return result

numbers1 = [3, 4, 5, 6]
numbers2 = [1, 2, 3, 4]
print(intersection(numbers1, numbers2))