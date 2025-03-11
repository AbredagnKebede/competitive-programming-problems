class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, mod = len(arr), 10**9 + 7
        left = [0]*n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        right = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i 
            stack.append(i)
            
        return sum(arr[i]*left[i]*right[i] for i in range(n))%mod