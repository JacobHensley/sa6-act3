people = ["Alice", "Bob", "Charlie"]

sorted_people = sorted(people, key=lambda x: (len(x), x[0]))
print(sorted_people)