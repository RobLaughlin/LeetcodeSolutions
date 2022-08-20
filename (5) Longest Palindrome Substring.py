# (5) Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# https://leetcode.com/problems/longest-palindromic-substring/

def LPS(s: str) -> str:
    # Stores PALINDROME_LENGTH->{p | s[p:p+PALINDROME_LENGTH] is a palindrome},
    # ex: palindromes[2] is the set of all 2 character palindromes, or rather their respective indices in s.
    palindromes = dict()
    
    # Similar to palindromes only in that special palindromes only hold palindromes with one repeated character.
    # ex: indices of "bbb" or "ddddd" in s.
    special_palindromes = dict()

    # Initialize the palindrome dictionaries while also adding all 1-length palindromes (every character in s)
    # Set current largest palindrome length 
    lpl = 1
    for char in range(lpl, len(s)+1):
        palindromes[char] = set()
        palindromes[1].add(char-1)
        special_palindromes[char] = set()
        special_palindromes[1].add(char-1)
    
    # Try to construct larger and larger palindromes until we can't anymore.
    # There are 2 rules we want to apply to our palindromes to ensure we capture all palindromes.

    # 1) If p is the index of the start of a palindrome, and s[p-1] == s[p+palindrome_len],
    # ...Then p-1 is a new palindrome of length palindrome_len+2.

    # 2) If p is the index of the start of a special palindrome, and s[p-1] == s[p] or s[p+palindrome_len] == s[p],
    # ...Then p-1 or p is a special palindrome of length palindrome_len+1, respectively.

    # Returns whether p is a valid index in the string s
    def exists(p):
        return p >= 0 and p < len(s)
    
    # Returns whether a palindrome set is empty or not.
    # Also returns true if l is not a valid key for either palindrome dictionary.
    def palindrome_empty(P, l):
        return not exists(l-1) or len(P[l]) == 0
    
    while True:
        # Find ALL palindromes and special palindromes of length lpl.
        # Build the next set of palindromes and special palindromes of length lpl+1.
        # After the set building process, 
        # if the palindromes set and the special palindromes sets are both empty for key=lpl+1,
        # then there are no new palindromes. and we return any largest palindrome by lpl.

        # 'Normal' palindromes, not 'aaa' or  'ccc' but 'abba' and 'acdca', etc.
        for p in palindromes[lpl]:
            l = p-1
            r = p+lpl
            if exists(l) and exists(r) and s[l] == s[r]:
                palindromes[lpl+2].add(l)
        
        # 'Special' palindromes, 'ccccc', 'eeee', etc.
        for p in special_palindromes[lpl]:
            l = p-1
            r = p+lpl
            if exists(l) and s[l] == s[p]:
                special_palindromes[lpl+1].add(l)
            if exists(r) and s[r] == s[p]:
                special_palindromes[lpl+1].add(p)
            
            # Also need to check for regular palindromes built from special palindromes. cases like "amma" built from "mm".
            if exists(l) and exists(r) and s[l] == s[r]:
                palindromes[lpl+2].add(l)
        
        print(palindromes)
        print(special_palindromes)
        print()
        if not palindrome_empty(palindromes, lpl+1) or not palindrome_empty(special_palindromes, lpl+1):
            lpl += 1
        elif not palindrome_empty(palindromes, lpl+2) or not palindrome_empty(special_palindromes, lpl+2):
            lpl += 2
        elif not palindrome_empty(palindromes, lpl):
            i = palindromes[lpl].pop()
            return s[i:i+lpl]
        else:
            i = special_palindromes[lpl].pop()
            return s[i:i+lpl]
            
if __name__ == '__main__':
    print(LPS("tattarrattat"))