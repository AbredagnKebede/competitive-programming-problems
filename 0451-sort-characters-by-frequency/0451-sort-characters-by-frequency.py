class Solution:
    def frequencySort(self, s: str) -> str:
        frqu_cnt = Counter(s)
        item = dict(sorted(frqu_cnt.items(), key = lambda x: x[1], reverse = True))
        result = ""
        for i in item:
            result += i*item[i]

        return result
        