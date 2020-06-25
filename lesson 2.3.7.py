a = int(input())
b = int(input())
x = [i for i in range(a, b+1) if i%3 == 0]
print(sum(x)/len(x))