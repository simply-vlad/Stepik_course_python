a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("\t", end="")
for j in range(c, d + 1):
    print("\t", j, sep="", end="")
for i in range(a, b+1):
    print("\n", i, end="")
    for x in range(c, d+1):
        print("\t", (i * x), end="")
    print(end="")