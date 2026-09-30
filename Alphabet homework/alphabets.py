a = "A"
b = "B"

print(not(a==b))

a = "C"
b = "C"


print(not(a==b))

letter = "D"

if not (letter == "A"):
    print("The letter is not A")

letter = "E"

if not (letter == "Z"):
    print("The letter is not Z")

a = "Python"
b = "python"

if not (a == b):
    print(a, "and", b, "are different.")