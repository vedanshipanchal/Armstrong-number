n = int(input("Enter a number that have 3 digits:"))

add = 0

temp = n

while temp >0:
    digit = temp % 10
    add += digit ** 3
    temp //=10

if n == add:
    print("armstrong number")
else:
    print("not an armstrong number")