#Program 2: Find the Largest Number in a List
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

largest = max(numbers)
print("The largest number is:", largest)
