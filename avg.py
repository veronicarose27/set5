N=int(input())
a=(list(map(int,input().split())))
sum=0
for i in range(N):
    sum=sum+a[i]
c=sum//N
print(c)
