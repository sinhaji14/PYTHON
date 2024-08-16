num=int(input("enter a number:  "))

count=0
if num>1:
    for i in range(2,num):
        if(num%i==0):
            count+=1
            print(num,"not a prime number")
        
    else:
                print(num,"it is a prime number")    
else:
    print("1 and 0 are not prime number")
