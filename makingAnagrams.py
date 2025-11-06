from collections import Counter

def makeAnagramS(s1,s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    deletions = 0
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        
        # Get the frequency of the current character in both strings
        freq1 = c1.get(char, 0)
        freq2 = c2.get(char, 0)
        
        # Add the absolute difference in frequencies to deletions
        deletions += abs(freq1 - freq2)
    return deletions

s1 = "cde"
s2 = "abc"
result = print(makeAnagramS(s1, s2)) # Expected: 3 (delete 'd', 'e'from s1; 'a', 'b' from s2)
