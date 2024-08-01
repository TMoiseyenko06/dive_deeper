#Task 1: Identify the greatest
#Task 2: Identify the smallest

num1,num2,num3 = input("Enter a list of numbers").split(",")
largest_number = 0
smallest_number = 0

if num1 > num2:
    largest_number = num1
    smallest_number = num2
else:
    largest_number = num2
    smallest_number = num1

if num3 > largest_number:
        largest_number = num3

if num3 < smallest_number:
     smallest_number = num3

print("The smallest number is: " + smallest_number)
print("The largest number is: " + largest_number)


