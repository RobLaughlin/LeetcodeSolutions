# 59. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# https://leetcode.com/problems/spiral-matrix-ii/

def generate_matrix(n):
    # There are 4 (really 5) states we are interested in, (0, 0), (0, k), (k, k), and (k, 0).
    # Describing top left, top right, bottom right, bottom left, in that order.
    # The final state we are interested in is at (1, 0), where the spiral ends after filling in the outer matrix.

    # Rather than (0, 0), we would like to start at some (i, i), an inner upper left corner of our matrix.
    # And follow the same filling process: (i, i) -> (i, i+k) -> (i+k, i+k) -> (i+k, i) -> (i+1, i).
    # We keep doing this filling process until k=0.

    # Initialize Matrix
    M = list()
    for _ in range(n):
        M.append(list())
        for _ in range(n):
            M[-1].append(0)

    # Fill in the outer matrix of size (k x k) starting at (i, i).
    # (i, i) top left,
    # (i, i+k-1) top right,
    # (i+k-1, i+k-1) bottom right,
    # (i+k-1, i) bottom left,
    # (i+1, i) top left down a row.
    def fill_outer(i, k, prev):
        # Edge case where we are asked to fill in the outer of a 1x1 matrix
        # if k == 1:
        #     prev += 1
        #     M[i][i] = prev
        #     return prev
        
        # Fill from (i, i) to (i, i+k-1) (top row)
        for j in range(k):
            prev += 1
            M[i][i+j] = prev

        # Fill from (i+1, i+k-1) to (i+k-1, i+k-1) (right column)
        for j in range(1, k):
            prev += 1
            M[i+j][i+k-1] = prev
        
        
        # Fill from (i+k-1, i+k-2) to (i+k-1, i) (bottom row)
        for j in range(1, k):
            prev += 1
            M[i+k-1][i+k-1-j] = prev

        
        # Fill from (i+k-2, i) to (i+1, i) (left column)
        for j in range(1, k-1):
            prev += 1
            M[i+k-1-j][i] = prev
        
        return prev

    prev = 0
    k = n
    i = 0
    while k > 0:
        prev = fill_outer(i, k, prev)
        k -= 2
        i += 1

    return M

if __name__ == "__main__":
    # Spiral matrices
    for i in range(5):
        print(generate_matrix(i))