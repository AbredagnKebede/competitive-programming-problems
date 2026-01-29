class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabit_color = Counter(answers)
        cnt = 0
        for key in rabit_color:
            expected = key + 1
            if rabit_color[key] % expected == 0:
                cnt += (rabit_color[key]//expected)*expected
            elif rabit_color[key] < expected:
                cnt += expected
            else:
                cnt += (rabit_color[key]//expected + 1)*expected
                
        return cnt 
