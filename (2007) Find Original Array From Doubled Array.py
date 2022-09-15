
from collections import Counter

"""
(2007) Find Original Array From Doubled Array
https://leetcode.com/problems/find-original-array-from-doubled-array/

An integer array original is transformed into a doubled array changed by appending twice the value
of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. 
If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
"""

def findOriginalArray(changed):
    # Odd number of elements in an array, no way it's a doubled array!
    if len(changed) % 2 == 1:
        return []

    # Sort the array and make a counter collection for the elements in the array
    changed = sorted(changed)
    elems = Counter(changed)
    original = []
    
    for c in changed:
        if c in elems and elems[c] <= 0:
            # In this case, we've already counted this element, so we can skip it.
            continue
        
        
        if 2*c in elems and elems[2*c] > 0:
            # We've found a pair! add the smaller c to the original array.
            original.append(c)
            elems[2*c] -= 1
            elems[c] -= 1
        else:
            # No pair found. Return an empty array.
            return []
        
    return original

if __name__ == '__main__':
    changed = [0,0,0,0]
    print(findOriginalArray(changed))