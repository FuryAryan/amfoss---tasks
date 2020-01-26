n , k = map(int,input().split()) 

a = list(map(int,input().split()))

score = a[k] 

count = 0

for i in range (len(a)):
    if(a[i] >= score and a[i] is not 0) : 
        count = count+1 

print(count)
