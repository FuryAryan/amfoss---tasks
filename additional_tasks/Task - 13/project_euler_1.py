n = int(input())
count = 0
extra = 0
additional = 0 
for i in range (0,n):
    j = int(input())
    for i in range (1,j):
        if i%3 == 0:
            count = count+1
    for k in range (1,j):
        if k%5==0:
            extra = extra + 1
    for z in range (1,j):
        if z%15:
            additional = additional+1
    
    zeb = count+extra - additional
    
    print(zeb)
            
    
            
    
    
    

