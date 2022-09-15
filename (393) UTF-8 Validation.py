"""
(393) UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/

Given an integer array data representing the data, 
return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).
"""

def charPreamble(char):
    # Returns the first 5 bits of a given character,
    # along with the type of preamble it is.

    # TYPES:
    # -1: Invalid preamble
    # 0: Seqential byte, starts with '10'
    # >= 1: Size of character in bytes

    # Split off insignificant digits
    for _ in range(3):
        char = (char - (char % 2)) // 2
    
    preamble = [0, 0, 0, 0, 0]
    for j in range(len(preamble)-1, -1, -1):
        digit = char % 2
        preamble[j] = digit
        char = (char - digit) // 2
    
    # 1 byte preamble
    if preamble[0] == 0:
        return preamble, 1
    
    # Sequential byte
    if preamble[1] == 0:
        return preamble, 0
    
    size = 2
    for p in preamble[2:]:
        if p != 1:
            return preamble, size
        
        size += 1

    # All 1's is an invalid preamble.
    return preamble, -1

def validUTF8(data):
    i = 0
    while i < len(data):
        char = data[i]
        _, pType = charPreamble(char)

        # char is either invalid or sequential
        if pType <= 0:
            return False
        
        # Encountered a standard 1 byte character, continue as normal
        if pType == 1:
            i += 1
            continue
        
        # Otherwise, need to process multiple bytes

        # The number of sequential bytes to process
        seq = pType - 1

        # Not enough sequential bytes, invalid character
        if i+seq >= len(data):
            return False
        
        for j in range(1, seq+1):
            nextByte = i+j
            _, sType = charPreamble(data[nextByte])

            # nextByte is not sequential, so char is invalid.
            if sType != 0:
                return False
        
        i += seq+1
    
    return True

if __name__ == '__main__':
    data = [235,140,4]
    print(validUTF8(data))