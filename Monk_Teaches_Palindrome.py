n=int(input())
for i in range(n):
    a=input()
    s=a[::-1]
    if a==s:
        if(len(a)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")