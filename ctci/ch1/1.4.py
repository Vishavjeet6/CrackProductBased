def is_palindrome_perm1(word):
    n = len(word)
    l = [0]*26
    for x in word:
        l[ord(x)-97] += 1
    c = 0
    for x in l:
        if x%2 != 0:
            c += 1
    if n%2==0:
        if c==0:
            return True
        return False
    else:
        if c==1:
            return True
        return False

def is_palindrome_perm(word):
    bit_vector = create_bit_vector(word)
    return bit_vector==0 or check_one_bit(bit_vector)

def create_bit_vector(word):
    bit_vector = 0
    for x in word:
        val = ord(x) - 97
        bit_vector = toggle(bit_vector, val) 
    return bit_vector

def toggle(bit_vector, val):
    mask = 1<<val
    if (bit_vector & mask) == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector

def check_one_bit(bit_vector):
    return (bit_vector & (bit_vector-1)) == 0

word = input()
print(is_palindrome_perm(word.lower()))