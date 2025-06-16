num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 = int(input("Enter third Number:"))

def compair(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest number")
    elif(b>a and b>c):
        print(f"{b} is greatest number")
    elif(c>a and c>b):
        print(f"{c} is greatest number")
    else:
        print("All three numbers are equal")
    

compair(num1, num2, num3)