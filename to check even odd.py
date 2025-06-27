# Program to find the maximum and minimum numbers in a list

# Input: Number of integers
n = int(input("Enter the number of integers: "))

# Input: List of integers
numbers = []
print("Enter the integers:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

# Initialize max and min with the first element of the list
maximum = numbers[0]
minimum = numbers[0]

# Iterate through the list to find max and min
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Output the results
print("The list of numbers:", numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)