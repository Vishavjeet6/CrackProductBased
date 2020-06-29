def one_away(word1, word2):
    if abs(len(word1)-len(word2)) > 1:
        return False
    d = False
    min1 = word1 if len(word1) < len(word2) else word2
    min2 = word2 if len(word1) < len(word2) else word1
    index1 = 0
    index2 = 0
    while(index1 < len(min1) and index2 < len(min1)):
        if min1[index1] == min2[index2]:
            index1 += 1
            index2 += 1
        else:
            if d:
                return False
            if len(min1) == len(min2):
                index1 += 1
                index2 += 1
            else:
                index2 += 1
                d = True
    return True

word1 = input()
word2 = input()
print(one_away(word1, word2))