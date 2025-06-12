num = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table for {num}:")

# Using for Loop
print("Using for Loop:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   

# Using while Loop with break
i = 1
while True:
    if i > 10:
        break
    print(f"{num} x {i} = {num * i}")
    i += 1

# In reverse order
print("In reverse order:")
i = 10
while True:
    if i == 0:
        break
    print(f"{num} x {i} = {num * i}")
    i -= 1 