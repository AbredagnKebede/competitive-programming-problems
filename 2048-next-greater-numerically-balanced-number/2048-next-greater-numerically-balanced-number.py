class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        value = n+1
        occurence = Counter(list(map(int, str(value))))
        while list(occurence.keys()) != list(occurence.values()):
            value +=1
            occurence = Counter(list(map(int, str(value))))
        return value