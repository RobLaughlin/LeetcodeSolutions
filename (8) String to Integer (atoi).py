"""
(8) String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
"""

VALID_DIGITS = set(map(lambda d: str(d), range(10)))

def myAtoi(s):
    digits = '0'
    sign = '+'

    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i >= len(s):
        return 0
    
    if s[i] not in VALID_DIGITS:
        if s[i] == '+' or s[i] == '-':
            sign = s[i]
        else:
            return 0
        
        i += 1
    
    while i < len(s) and s[i] in VALID_DIGITS:
        digits += s[i]
        i += 1
    
    maxVal = 2**31
    n = int(sign + digits)
    n = min(n, maxVal-1)
    n = max(n, -maxVal)

    return n

if __name__ == '__main__':
    s = "4193 with words"
    print(myAtoi(s))