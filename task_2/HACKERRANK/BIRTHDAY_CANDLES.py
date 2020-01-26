age_of_girl = int(input())
size_of_candles = list(map(int,input().split()))[:age_of_girl]
max_height = max(size_of_candles)

count = 0

for i in range(len(size_of_candles)):
    if (size_of_candles[i] == max_height):
        count = count + 1

print(count)
