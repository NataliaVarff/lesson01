a = int(input("введите начальную точку"))
b = int(input("введите конечную точку"))
days = 1
while b - a > 0:
      a = a * 1.1
      days += 1
print(days)
