'''
Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''

class RandomizedSet:

    def __init__(self):
        
        self.d = {}

    def insert(self, val: int) -> bool:
        
        if val in self.d:
            return False
        else:
            self.d[val] = '1'
        return True

    def remove(self, val: int) -> bool:
        
        try: 
            del self.d[val]
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.d.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
#Runtime: 388 ms
#Memory Usage: 18 MB