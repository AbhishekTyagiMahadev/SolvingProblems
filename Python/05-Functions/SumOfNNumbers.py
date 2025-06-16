def cal(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    print(f"Sum of first {num} natural numbers is {sum}")

cal(int(input("Enter a natural Number:")))