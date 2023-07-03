numbers = [
    55, 985, 12, 35, 46, 78, 9, 12, 1, 56, 15, 0, 13, 18, 19, 22553, 49, 289, 264
]

s = 0
for num in numbers:
    if (num % 2 == 0): s += num

print(s)