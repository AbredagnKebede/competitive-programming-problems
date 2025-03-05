class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            if stack:
                prev = [0,0]
                while stack and stack[-1][1] < val:
                    prev = stack.pop()
                    answer[prev[0]] = i - prev[0]
    
            stack.append([i,val])

        return answer
