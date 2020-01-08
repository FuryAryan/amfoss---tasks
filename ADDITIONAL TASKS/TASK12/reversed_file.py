import string

def de_xor(x):
    return ''.join(chr(ord(k)^10) for k in x)

def de_shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i)-3)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)-3)%26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i)-3)%10])
    return n
def decode(x):
    return bytearray.fromhex(x).decode()
    
your_code=(de_shift(de_xor(decode('667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268'))))
print(your_code)
string=""
for i in your_code:
    string+=i
print(string)

#OUTPUT I GOT : inctfjr3v3r533n61n33r1n61550345y
#['i', 'n', 'c', 't', 'f', 'j', 'r', '3', 'v', '3', 'r', '5', '3', '3', 'n', '6', '1', 'n', '3', '3', 'r', '1', 'n', '6', '1', '5', '5', '0', '3', '4', '5', 'y']
    

    

   