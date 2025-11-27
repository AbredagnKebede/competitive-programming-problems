class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        alphabet = defaultdict(int)
        ans = []
        for word in words2:
            wordcnt = Counter(word)
            for letter in wordcnt:
                alphabet[letter] = max(alphabet[letter], wordcnt[letter])

        for w in words1:
            w_c = Counter(w)
            for i in alphabet:
                if i not in w_c:
                    break
                else:
                    if w_c[i] < alphabet[i]:
                        break
            else:
                ans.append(w)        
        return ans
