def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a numbber to calculate its factorial:"))
print(f"Factorial of {n} is {factorial(n)}")