class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_frq = defaultdict(int)
        left, right = 0, 0 
        longest = 0 
        while right < len(s):
            if count_frq[s[right]] < 1:
                count_frq[s[right]] += 1
                right += 1
            else:
                while count_frq[s[right]] > 0:
                    count_frq[s[left]] -= 1
                    left += 1
            longest = max(longest, right - left)
        
        return longest