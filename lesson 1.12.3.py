a = float(input())
b = float(input())
c = input()

if b == 0 and c == "div":
    print ("Деление на 0!")
elif b == 0 and c == "mod":
    print ("Деление на 0!")
elif b == 0 and c == "/":
    print ("Деление на 0!")
elif b != 0 and c == "div":
    print (a // b)
elif b != 0 and c == "mod":
    print(a % b)
elif c == "pow":
    print (a ** b)
elif b != 0 and c == "/":
    print (a / b)
elif c == "*":
    print (a * b)
elif c == "-":
    print (a - b)
elif c =="+":
    print(a + b)