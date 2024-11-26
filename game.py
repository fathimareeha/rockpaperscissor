import random
count=0
count1=0

while(True):
    print("1.play","2.exit")
    num=int(input("enter a number"))
    if  num==1:
        a=["rock","paper","scissor"]
        b=input("enter your choice ")
        a=(random.choice(a))
        print(a)
        if (a=="rock" and b=="paper") or (a=="paper" and b=="scissor") or (a=="scissor" and b=="rock"):
            print("u win")
            count=count+1
           
        
        elif (a=="paper" and b=="rock") or (a=="scissor" and b=="paper") or (a=="rock" and b=="scissor"):
            print("computer win")
            count1=count1+1
           
        
        elif a==b:
            print("tie")
    else:
        print("exit")
        break
print("user score",count)
print("computer score",count1)
    
    


    
    

    
