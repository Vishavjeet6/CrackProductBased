def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    l = [0]*26
    for x in string1:
        l[ord(x)-97] += 1
    for x in string2:
        l[ord(x)-97] -= 1
        if l[ord(x)-97] <0:
            return False
    return True

word1 = input()
word2 = input()
print(is_permutation(word1, word2))