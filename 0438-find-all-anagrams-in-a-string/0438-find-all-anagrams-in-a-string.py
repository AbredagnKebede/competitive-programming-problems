class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        ans = []
        for i in range(len(s)-len(p) + 1):
            if Counter(s[i:i+len(p)]) == target:
                ans.append(i)
        return ans