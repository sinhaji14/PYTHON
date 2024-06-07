#open
"""with open("practice.txt","w") as f :
    f.write("Hi everyone \n we are learning File I/O \n")
    f.write("using Java.\n I like programming in Java")"""

"""with open("practice.txt","r") as f :
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
with open("practice.txt","w") as f :
    f.write(new_data)"""
def check_word():
    word = "learning"
    with open("practice.txt","r") as f:
              data=f.read()
    if(data.find(word)!=-1):
                            print("found")
    else:
              print("not found") 
check_word()