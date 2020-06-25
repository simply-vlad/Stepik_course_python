s = input()
count = 1
z = 0
while (z+1)<len(s):
    if s[z] == s[z+1]:
        count += 1
    else:
        print(s[z] + str(count), end ="")
        count = 1
    z += 1

print(s[z] + str(count))