data = []
for i in range(4):
    name = input(f"Enter the name of person {i+1}: ")
    age = int(input(f"Enter the age of person {i+1}: "))
    shoe_size = float(input(f"Enter the shoe size of person {i+1}: "))
    data.append([name, age, shoe_size])
remove_name = input("Enter the name of the person you want to remove from the list: ")
for row in data:
    if row[0] == remove_name:
        data.remove(row)
        break
for row in data:
    print(row)
