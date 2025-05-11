class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)
        cur_window = Counter(s2[:len(s1)])

        if cur_window == s1_cnt:
                return True

        for i in range(len(s1), len(s2)):
            char_prev = s2[i-len(s1)]
            char_cur = s2[i]

            cur_window[char_prev] -= 1
            cur_window[char_cur] += 1
            if cur_window[char_prev] == 0: del cur_window[char_prev]
            
            if cur_window == s1_cnt:
                return True
            
        return False