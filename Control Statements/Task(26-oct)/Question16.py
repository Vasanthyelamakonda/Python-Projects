n = int(input("Enter the value of n: "))
t = n

# Upper half of the pattern
for i in range(n):
    # Left side stars
    for j in range(i + 1):
        print("*", end=" ")
    # Middle spaces
    for j in range(t * 2 - 2):
        print(" ", end=" ")
    # Right side stars
    for j in range(i + 1):
        print("*", end=" ")
    print()
    t -= 1

s = 1
# Lower half of the pattern
for i in range(n - 1, 0, -1):
    # Left side stars
    for j in range(i):
        print("*", end=" ")
    # Middle spaces
    for j in range(s * 2):
        print(" ", end=" ")
    # Right side stars
    for j in range(i):
        print("*", end=" ")
    print()
    s += 1
