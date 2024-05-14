# Anagram is a word that is form by arranging the words 

def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    # Create dict to store character counts for each string
    count_s = {}
    count_t = {}

    #populate count_s
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    #populate count_t
    for char in t:
        count_t[char] = count_t.get(char,0)+1

    return count_s == count_t


print(isAnagram("moon","noon"))