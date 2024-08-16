total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    choice = input("Do you want to include this number? (y/n) ")
    if choice.lower() == "y":
        total += number
print("The total is", total)

