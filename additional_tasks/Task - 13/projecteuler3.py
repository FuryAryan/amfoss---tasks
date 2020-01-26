n=int(input())
l=[]
prime=[]
for i in range(n):
    count=[]
    x=int(input())
    l.append(x)
    for k in range(1,x):
        if(x%k==0):
            count.append(k)
    prime.append(count)
for i in range(len(prime)):
    if(len(prime[i])==1):
        print(l[i])
    else:
        print(max(prime[i]))
