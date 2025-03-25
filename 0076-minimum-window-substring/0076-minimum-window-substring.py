class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = Counter(t)
        s_cnt = defaultdict(int)
        have , need = 0, len(t_cnt)
        min_len = float('inf')
        min_window = ""
        left = 0
        for right in range(len(s)):
            cur = s[right]
            s_cnt[cur] += 1

            if cur in t_cnt and s_cnt[cur] == t_cnt[cur]:
                have += 1
            
            while have == need:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                s_cnt[s[left]] -= 1
                if s[left] in t_cnt and s_cnt[s[left]] < t_cnt[s[left]]:
                    have -= 1
                left += 1 
        
        return min_window