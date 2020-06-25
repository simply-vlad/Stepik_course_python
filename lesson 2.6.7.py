a = int(input())
b = a
c = 0+abs(b**2)
while b!=0:
    a = int(input())
    b = b + a
    c = c + abs(b)**2
    if b == 1:
        break
print(c)