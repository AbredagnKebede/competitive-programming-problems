class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)   
        for start, end, direction in shifts:
            if direction == 1:   
                diff[start] += 1
                diff[end + 1] -= 1
            else:  
                diff[start] -= 1
                diff[end + 1] += 1
 
        shift = 0
        result = []
        for i, char in enumerate(s):
            shift += diff[i]   
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))   
            result.append(new_char)

        return "".join(result)
