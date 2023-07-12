a, b = 0, 1
print(a)

while b <= 50:
    print(b)
    a, b = b, a + b     # a & b should reassign in same line
    # a = b
    # b = a + b
