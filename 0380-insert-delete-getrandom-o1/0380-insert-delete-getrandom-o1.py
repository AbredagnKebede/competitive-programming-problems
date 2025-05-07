class RandomizedSet:

    def __init__(self):
        self.random_set = []
        self.indexmap = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.indexmap:
            self.random_set.append(val)
            self.indexmap[val] = len(self.random_set) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indexmap:
            index = self.indexmap[val]
            last_val = self.random_set[-1]
            self.indexmap[last_val] = index
            self.random_set[index], last_val = last_val, self.random_set[index]
            self.random_set.pop()
            del self.indexmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.random_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()