def reverseInt(x):
    s = str(x)
    sign = '+'
    if s[0] == '-':
        s = s[1:]
        sign = '-'
    
    s = sign + "".join(reversed(s))
    x = int(s)
    
    maxInt = 2**31
    if x < -maxInt or x > maxInt-1:
        return 0
    
    return x

if __name__ == '__main__':
    x = 123
    rev = reverseInt(x)
    print(rev)