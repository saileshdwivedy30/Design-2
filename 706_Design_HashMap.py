# This approach uses an array of fixed size (based on the problem constraints) to store key-value pairs.
# Each key value pair is stored in a list at an index corresponding to the hash of the key.
# If multiple keys hash to the same index, a linked list is used to store the pairs at that index.

# TC for all ops - avg: O(1) but O(n) incase of all keys hashing to same index
# SC - avg: O(n), no of key value psairs

class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 1
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.map[index] is None:
            self.map[index] = []
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        if self.map[index] is not None:
            for k, v in self.map[index]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.map[index] is not None:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    del self.map[index][i]
                    return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)