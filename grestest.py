num1= int(input("enter the first value "));
num2= int(input("enter the second value "));
num3= int(input("enter the third value "));

if num1>num2 and num1>num3:
    print("num1 is greater");
elif num2>num1 and num2>num3:
    print("num2 is greater");
else:
    print("num3 is greater");
