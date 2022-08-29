n=int(input())
for i in range(0,n):
    s=input()
    c=0
    for j in s:
        if j in '0123456789':
            c+=1
    if(c==len(s)):
        print("True")
    else:
        print("False")