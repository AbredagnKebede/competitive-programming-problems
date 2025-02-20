class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums = [ord(char) - ord('a') for char in s]

        prefix = [0]*(len(s)+1)
        for left, right, d in shifts:
            prefix[right+1] += 1 if d else -1
            prefix[left] += -1 if d else 1
        move = 0 
        for i in reversed(range(1, len(prefix))):
            move += prefix[i]
            nums[i-1] = (nums[i-1] + move)%26
        
        return "".join(chr(num + ord('a')) for num in nums)
        