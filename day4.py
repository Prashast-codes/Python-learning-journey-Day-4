# In todays session we are practising questions of mix up of what we have learn:
# Question no. 1. : grade checker :

marks = int(input("please enter your marks:"))
if marks >= 90 :
    print("grade : A+")
elif marks >= 80 :
    print("grade : A")
elif marks >= 70 :
    print("grade : B+")
elif marks >= 60 :
    print("grade : C")
elif marks >= 50 :
    print("grade D")
elif marks >= 40 :
    print("grade : E")
else :
    print("grade : F [fail]")

# Question no. 2. : even and odd checker in 1 to 5 :

number = int(input("pls enter a number:"))

while number <= 5 :
    if number % 2 == 0 :
        print("EVEN")
    else:
        print("ODD")
    number += 1

# Question no. 3. : check wether the number is positive, negative or zero :

number =  int(input("pls enter a number:"))
if number > 0 : 
    print("positivef num")
elif number < 0 :
    print("negative num")
else :
    print("zero")


