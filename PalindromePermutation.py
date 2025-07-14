def permute_palindrome(st):
    frequencies = {}
    for i in st:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    count = 0
    for ch in frequencies.keys():
        if frequencies[ch] % 2:
            count += 1

    if count <= 1:
        return True
    else:
        return False
    
print(permute_palindrome("carrace"))
