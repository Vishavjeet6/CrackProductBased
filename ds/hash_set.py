#705. Design HashSet leetcode


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2096
        self.hash_table = [Bucket() for i in range(self.key_space)]        
    def add(self, key: int) -> None:
        hash_key = key%self.key_space
        self.hash_table[hash_key].update(key)

    def remove(self, key: int) -> None:
        hash_key = key%self.key_space
        self.hash_table[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = key%self.key_space
        return self.hash_table[hash_key].get(key)
        
class Bucket:
    
    def __init__(self):
        self.bucket = []
        
    def update(self, key):
        for x in self.bucket:
            if x==key:
                break
        else:
            self.bucket.append(key)
    
    def remove(self, key):
        for i,x in enumerate(self.bucket):
            if x==key:
                del self.bucket[i]
    
    def get(self ,key):
        for x in self.bucket:
            if x==key:
                return True
        return False
        
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
