import sys
import random
print("Введи кол-во кол-во столбцов в игре (ОБЯЗАТЕЛЬНО меньше 51)")
n = int(input())
a = []
if n>50:
    print("А, ок, понял")
    sys.exit()
for i in range (n):
    a.append(["□"]*n)
print("   ", end="")
for i in range(n):
    if i > 9:
        print(i + 1, end=" ")
    else:
        print(i+1, end="  ")
print()
for i in range(len(a)):
    if i < 9:
        print(i + 1, end="  ")
    else:
        print(i+1, end=" ")
    for j in range(len(a[i])):
        print(" "+ a[i][j], end=" ")
    print()
