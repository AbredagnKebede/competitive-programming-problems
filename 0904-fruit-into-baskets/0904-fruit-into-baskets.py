class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_tree = 0
        left = 0 
        freq = defaultdict(int )
        for i in range(len(fruits)):
            freq[fruits[i]] += 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1 
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_tree = max(max_tree, i - left + 1)
        return max_tree
                
