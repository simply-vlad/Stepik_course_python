x = [int(i) for i in input().split()]
for i in set(x):
    b = x.count(i)
    if b > 1:
        print(i, end =" ")