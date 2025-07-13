def first_unique_char(s):

    character_count = {} 
    string_length = len(s)  

    for i in range(string_length): 
        if s[i] in character_count:
            character_count[s[i]] += 1
        else:
            character_count[s[i]] = 1

    for i in range(string_length):
        if character_count[s[i]] == 1:
            return i
            
    return -1

print(first_unique_char("abaabbcc"))
print(first_unique_char("abaabbcch"))
