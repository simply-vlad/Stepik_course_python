c=int(input())
n = c%100
if n>20:
    n=n%10

if n==1:
    print(str(c) +" программист")
elif (n>1 and n<5):
    print(str(c)+ " программиста")
else:
    print(str(c) + " программистов")