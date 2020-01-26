n = int(input())
for deb in range (0,n):
    letter = str(input())
    length_of_string = len(letter)
    
    if length_of_string <= 10:
        print(letter)
    else:
        print(letter[0]+str(length_of_string)+[length_of_string-1])
    