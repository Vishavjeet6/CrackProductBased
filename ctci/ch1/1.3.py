def urlify(word,n):
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

word = input()
n = int(input())
print(urlify([*word],n))
