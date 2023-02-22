numbers = input("Enter a list of numbers, separated by commas: ").split(",")
numbers = [int(num) for num in numbers]
positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print("Positive numbers From the given range are:", positive_numbers)
