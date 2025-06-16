n = int(input("Enter the value of n :"))


def pattern(n):
    for i in range(n, 0, -1):
        print('*' * i)
    
pattern(n)


