n , k = map(int,input().split()) #here taking two inputs as n , k (where k kth place ) and n is number of places

a = list(map(int,input().split())) # now taking the score here and representing with a

score = a[k] #here a of k means kth place in a

count = 0 #now assuming count be 0

for i in range (len(a)): #and taking acess for every element in the list we use here for loop
    if(a[i] >= score and a[i] is not 0) : #for qualifying to next round the score must be greater than kth place score or equal to it
        count = count+1 #it is the total players qualified for next round

print(count)
