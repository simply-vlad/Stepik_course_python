#x = input().lower()
#a = 0
#b = 0
#for nucl in x:
#    if nucl == "g":
#        a+=1
#for nucl in x:
#    if nucl == "c":
#        b+=1
#print(float((a+b)/len(x))*100)

# short version
# x = input()
# a1 = x.upper().count("c".upper())
# a2 = x.upper().count("g".upper())
# z = a1+a2
# print(z/len(x)*100)

###### very short version
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)
