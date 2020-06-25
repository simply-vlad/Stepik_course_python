a = input().split()
if len(a) == 1:
    print(a[0])
elif len(a) > 1:
    b = [int(a[i-1])+int(a[i+1]) for i in range (-1, len(a)-1)]
    for i in range (1, len(b)):
        print(b[i], end = " ")
    print(b[0])