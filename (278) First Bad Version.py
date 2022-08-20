"""
(278) First Bad Version
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

https://leetcode.com/problems/first-bad-version/
"""

# Implemented by leetcode, see website
def isBadVersion(i):
    return True

def firstBadVersion(self, n: int) -> int:
    l = 1
    r = n

    i = 0
    while True:
        i = (r + l) // 2
        isBad = isBadVersion(i)

        if isBad:
            # This is ideal, this is the first bad version
            if (i > 1 and not isBadVersion(i-1)) or i==1:
                return i
            
            # case when (i-1) is also a bad version. Keep searching!
            r = i-1
        else:
            # If we found a good version, then search more to the right!
            l = i+1