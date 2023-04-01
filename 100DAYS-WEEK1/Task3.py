a=[1,2,3]
n=eval(input())
if type(n)!=int:
    a.extend(n)
else:
    a.append(n)
 print(a)       