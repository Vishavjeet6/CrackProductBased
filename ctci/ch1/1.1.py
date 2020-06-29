def is_unique(word):
    l=[0]*26
    for x in word:
        l[ord(x)-97] += 1
        if(l[ord(x)-97] > 1):
            print("No")
            break
    else:
        print("Yes")

# no ds
def is_unique1(word):
    checker = 0
    for x in word:
        val = ord(x)-97
        if(checker & (1<<val) > 0):
            print("No")
            break
        checker |= (1<<val)
    else:
        print("Yes")
     

word = input()
is_unique(word)
is_unique1(word)