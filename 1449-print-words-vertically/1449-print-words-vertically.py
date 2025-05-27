class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_new = list(s.split())
        max_len = max((len(i) for i in s_new), default=0)

        #by adding an empty string making all words have equal len
        for i in range(len(s_new)):
            if len(s_new[i]) < max_len:
                s_new[i] = s_new[i].ljust(max_len)

        result = ["".join(i).rstrip() for i in zip(*s_new)]

        return result
        