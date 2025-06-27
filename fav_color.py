fav_color = input("What is your favorite color = ")
print(f"Your favorite color is {fav_color}.")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter a third number: "))

# Calculate the sum of the three numbers   
product = num1 * num2 * num3
average = (num1 + num2 + num3) // 3
print(f"The product of the three numbers is {product}.")
print(f"The average of the three numbers is {average}.")

# questiob 3
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

z = (x**2 + y**2 + 2*x*y)  / (x + y + 1)
print(f"The result of the division is {z}.")


# question 4
height = float(input("Enter your height : "))
breadth = float(input("Enter your breadth : "))
area = (1/2) * height * breadth
print(f"The area of the rectangle is {area}.")

# question 5
m = int(input("Enter a value: "))
n = int(input("Enter another  value: "))

m = m + n
n = m - n
m = m - n
print(f"m = {m}, n = {n}.")
