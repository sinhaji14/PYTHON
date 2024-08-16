#while loop
"""n = int(input("enter number:"))
i = 0
while i<=10:
    print(n*i)
    i+=1"""

"""nums =[1,4,9,16,25,36,49,64,81,100] #traverse
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1 """

"""nums =(1,4,9,16,25,36,49,64,81,100)#linera search method used here
x= 36
i=0
while i<len(nums):
  if(nums[i]==x):
    print("found at ",i)
    break
  else:
    print("not found")  
    i+=1


print("end of loop")    """
#for loop
n= int(input("enter n"))
fact=1
for i in range(1,n+1):#range(start,stop,step)
    fact *=i
   
    
    
print("the factorial is",fact)   
    

