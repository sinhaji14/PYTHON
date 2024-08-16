#recursive function
"""def sumnatno(n):
    if(n==0):
        return 0
    else:
        return sumnatno(n-1)+ n
sum=sumnatno(5)

print(sum)"""

#print all element in a lsit

def print_list(list , idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banna"] 

print_list(fruits,2)