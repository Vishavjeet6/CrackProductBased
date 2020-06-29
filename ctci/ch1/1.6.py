def compress_string(word):
    count = 1
    ans = ""

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            ans += word[i] + str(count)
            count = 1
    if count > 0:
        ans += word[-1] + str(count)
    else:
        ans += word[-1] + "1"
    if(len(ans) > len(word)):
        return word
    else:
        return ans
    


word = input()
print(compress_string(word.lower()))