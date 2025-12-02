a = int(input("Enter any number: "))

if a % 2 == 0:
    n = a - 1
else:
    n = a

for i in range(1, n + 1):
    if i < n:
        print(2*i - 1, end=", ")
    else:
        print(2*i - 1)
