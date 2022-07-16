n=int(input())
l=list(map(int,input().split( )))
p=[]
p=sorted(list(set(l)))
if(n>=3):
    print(p[-3])
else:
    print(max(p))