def triplets(a,b):

    child = [0,0]

    if (a[0]>b[0]):
    child[0] = child[0]+1
    elif (a[0]<b[0]):
    child[0] = child[1] = child[1] + 1
    if (a[1]>b[1]):
    child[0] = child[0]+1
    elif (a[1]<b[1]):
    child[1] = child[1] + 1
    if (a[2]>b[2]):
    child[0] = child[0]+1
    elif (a[2]<a[2]):
    child[1] = child[1]+1

    print(child[0],child[1])

a = list(map(int,input().split()))[:3]
b = list(map(int,input().split()))[:3]
triplets(a,b)
