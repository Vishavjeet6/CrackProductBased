def urlify1(word,n):
    space_count = 0
    for i in range(n):
        if(word[i]==" "):
            space_count += 1
    index = n + 2*space_count
    if n < len(word):
        word = word[:n]
    for i in range(n-1, -1, -1):
        if(word[i] == " "):
            word[index] = "0"
            word[index-1] = "2"
            word[index-2] ="%"
        else:
            word[index-1] = word[i]
            index -= 1 


def urlify(word, n):
    word = word.strip()
    space_count = word.count(" ")
    true_length = len(word) + 2*space_count
    word = list(word)
    for i in range(len(word), true_length):
        word.append('*')
    j = true_length-1
    for i in range(n-1,-1,-1):
        if(word[i] == " "):
            word[j] = "0"
            word[j-1] = "2"
            word[j-2] = "%"
            j -= 3
        else:
            word[j] = word[i]
            j -= 1
    return ''.join(word)



    


print(urlify1([*word],n))
print(urlify("Mr John Smith   ", 13))
print(urlify("Mr John Smith", 13))
print(urlify("v s", 3))