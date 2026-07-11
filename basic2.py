# Largest Element in a List:

numbers = [12, 45, 8, 67, 23]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest =", largest)