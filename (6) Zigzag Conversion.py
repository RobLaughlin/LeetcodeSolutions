# (6) Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows.
# https://leetcode.com/problems/zigzag-conversion/

def chunks2str(chunks):
    return "".join(map(lambda chunk: "".join(chunk), chunks))

def convert(s, rows):
    # Chunks is a list of rows.
    # c points to the current chunk we are working with.
    # direction is whether we are moving forward (1) or backward (-1) regarding which row to move to next.
    chunks = list()
    c = 0
    direction = 1

    # Initialize how many chunks we need for each row.
    # May terminate early if we dont need as many chunks as rows.
    for r in range(rows):
        chunks.append(list())
        if r >= len(s):
            return chunks2str(chunks)

        chunks[r].append(s[r])
    
    # Begin processing s in zigzag order.
    c = len(chunks)-1
    direction = -1

    for i in range(rows, len(s)):
        # When we hit the "top" or "bottom", swap directions.
        # If the number of rows is only 1, then c stays fixed at 0.
        if rows != 1:
            c += direction
            if c == 0 or c == rows-1:
                direction *= -1
        
        chunks[c].append(s[i])
        
    return chunks2str(chunks)

if __name__ == '__main__':
    s = "abc"
    rows = 1

    print(convert(s, rows))