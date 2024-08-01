#Task 1: Leap Year Checker

provided_year = int(input("Please Enter a year:"))
leap_year = False

if (provided_year % 4 == 0 and not provided_year % 100 == 0) or (provided_year % 100 == 0 and provided_year % 400 == 0):
    leap_year = True

print("Leap Year: " + leap_year)
