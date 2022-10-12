s=input()
I=0
D=len(s)
for i in s:
    if i=='I':
        print(I,end=" ")
        I+=1
    if i=='D':
        print(D,end=" ")
        D-=1
if s[len(s)-1]=='I':
    print(I)
else:
    print(D)