'''
 Iterator for Combination

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 
'''
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                yield from combinations(cur, i + 1)
                cur.pop()
        self.combos = combinations([], 0)
        self.current = True
        self.hasNextCalled = False
                
        

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current
        

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#Runtime: 52 ms
#Memory Usage: 15.5 MB