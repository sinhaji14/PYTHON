"""marks=[82,89,99,56]
marks.append(45)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(1,88)
print(marks)
marks.remove(99)
marks.pop(1)
print(marks)"""  
"""movies1 =input("enter your movie1")
movies2 = input("movie2 ")
movies3=input("movie 3")

fav_movie = [movies1,movies2,movies3]
print(fav_movie)
"""
#palindrome
list1=[1,2,1]
list2=[1,2,3]
cop_list1 =list1.copy()
cop_list1.reverse()
if(list1== cop_list1):
    print("palindrome")
else:
    print("not a palindrome")    