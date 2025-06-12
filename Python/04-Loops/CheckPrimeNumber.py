number = int(input("Enter a number to check if it is prime: "))
for num in range(2, number):
    if number % num == 0:
        print(f"{number} is not a prime number.")
        break
    else:
        print(f"{number} is a prime number.")
        break