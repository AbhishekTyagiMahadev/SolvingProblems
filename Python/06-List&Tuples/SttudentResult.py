result = []
total = 0
for i in range(5):
    marks = int(input(f"Enter the marks of subject{i+1}:"))
    total += marks
    result.append(marks)
result.sort()
print(f"Result:{result}")
print(f"Total Marks:{total}")
print(f"Total Percentage:{total/len(result)}")