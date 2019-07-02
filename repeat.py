m,k=map(int,input().split())
a=list(map(int,input().split()))
l=len(a)
count=0
for i in range(0,m):
    if(a[i]==k):
        count=count+1
print(count)
    
