num = float(input("Enter a number: "))
if num < 0:
    print("Square root of a negative number is not a real number.")
else:  
    result = num ** 0.5
    print(f"The square of {num} is {result}")