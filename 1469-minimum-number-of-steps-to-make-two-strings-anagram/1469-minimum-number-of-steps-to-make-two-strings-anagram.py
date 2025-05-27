class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        print(count_s, count_t)
        count = 0
        for i in count_s:
            if i not in count_t:
                count += count_s[i]
            elif i in count_t and count_t[i] < count_s[i]:
                count += abs(count_t[i]-count_s[i])
        return count