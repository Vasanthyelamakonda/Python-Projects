n = int(input("Enter the value of n: "))
t = n

for i in range(n):
    a = 0
    b = chr(i + 65)
    for j in range(i + 1):
        print(chr(a + 65), end=" ")
        a += 1
    for j in range(t * 2 - 2):
        print(" ", end=" ")
    for j in range(i + 1):
        print(b, end=" ")
        b = chr(ord(b) - 1)
    print()
    t -= 1

s = 1
for i in range(n - 1, 0, -1):
    a = 0
    b = chr(i + 96)
    for j in range(i):
        print(chr(a + 97), end=" ")
        a += 1
    for j in range(s * 2):
        print(" ", end=" ")
    for j in range(i):
        print(b, end=" ")
        b = chr(ord(b) - 1)
    print()
    s += 1

