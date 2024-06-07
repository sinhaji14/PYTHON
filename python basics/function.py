# print the length of a list
cities = ["delhi","gurgaon","noida","pune","patna"]
heroes =["thor", "ironman","batman","shaktimaan" ]
print(heroes[0],end=" ")
print(cities[0],end=" ")

def print_len(list):
    print(len(list))



def print_list(list):
    for item in list:
        print(item, end=" ")

  
  
print_list(cities)      