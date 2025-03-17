# Get input and split into integers
numbers = [int(x) for x in input().split()]

# Sum only positive numbers
result = sum(num for num in numbers if num > 0)

# Print result
print(result)