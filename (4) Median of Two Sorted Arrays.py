# (4) Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# https://leetcode.com/problems/median-of-two-sorted-arrays/

def medianFromSortedArrays(A, B):
    # For any sorted array S = merge(A, B), we can separate S into 2 partitions.
    # 1) len(S) even, S = [L | R]
    # 2) len(S) odd, S = [L |S[m]| R].
    # The goal is to find such a partition L, then the element either immediately following L,
    # or (the maximal element of L + the minimal element of R) // 2 will be our median.
    
    # Some annoying edge cases
    if len(A) == 0 or len(B) == 0:
        Aodd = len(A) % 2
        Bodd = len(B) % 2
        if len(A) == len(B):
            return None
        elif len(A) == 0:
            return B[(len(B) // 2)] if Bodd else (B[(len(B) // 2)] + B[(len(B) // 2)-1]) / 2
        else:
            return A[(len(A) // 2)] if Aodd else (A[(len(A) // 2)] + A[(len(A) // 2)-1]) / 2

    # Size of our sorted array
    size = len(A) + len(B)

    # Always make A the shorter array
    if len(A) > len(B):
        A, B = B, A
    
    # The left-index of the median in our sorted (A+B) merged array.
    # Left-index means that if len(A)+len(B) is even, then the true median is (A+B)[m]+(A+B)[m+1] // 2.
    # Otherwise if len(A)+len(B) is odd, the true median is exactly (A+B)[m].
    m = (size // 2) - 1

    # The goal is to find indices i and j,
    # such that A[i] <= B[j+1] and B[j] <= A[i+1].
    # This is the case that A[:i] and B[:j] form the partition L.
    # We will use binary search to find our index i,
    # So we create a search space for the indices of A.
    l = 0
    r = len(A) - 1

    # Note that the index j immediately follows from finding i.
    # (i+1) + (j+1) will be the total length of our partition P (not necessarily L yet),
    # but (i+1) + (j+1) = i+j+2 = len(P) = m+1
    # So we can uniquely determine j if we know A, B, m, and i.
    # In short, we can only search for i then calculate j later.
    odd = size % 2
    inf = float("infinity")
    neginf = float("-infinity")
    while True:
        i = (l + r) // 2
        j = m - i - 1

        # Some quick bounds fixing
        Aleft = A[i] if i >= 0 else neginf
        Aright = A[i+1] if i+1 < len(A) else inf
        Bleft = B[j] if j >= 0 else neginf
        Bright = B[j+1] if j+1 < len(B) else inf

        if Aleft > Bright:
            r = i-1 # Grow A, Shrink B.
        elif Bleft > Aright:
            l = i+1 # Grow B, Shrink A.
        else:
            # Hit our target case!
            # A[i] <= B[j+1] and B[j] <= A[i+1]
            if odd:
                return min(Aright, Bright)
            
            return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            
if __name__ == "__main__":
    A = sorted([1,2])
    B = sorted([3,4])
    print(medianFromSortedArrays(A, B))