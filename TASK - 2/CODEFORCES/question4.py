number_of_statments = int(input())

count = 0

for i in range(0,number_of_statments):
    inp = input()
    if '++' in inp:

        count = count+1

    elif '--' in inp:

        count = count-1

print(count)
