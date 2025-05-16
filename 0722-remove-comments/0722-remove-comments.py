from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        commented = False  
        result = []  
        stack = []   
        
        for line in source:
            i = 0
            if not commented:
                stack = []  

            while i < len(line):
                if not commented and i + 1 < len(line) and line[i:i+2] == "/*":
                    commented = True
                    i += 1   
                elif commented and i + 1 < len(line) and line[i:i+2] == "*/":
                    commented = False
                    i += 1  
                elif not commented and i + 1 < len(line) and line[i:i+2] == "//":
                    break   
                elif not commented:
                    stack.append(line[i])
                i += 1 

            if stack and not commented:   
                result.append("".join(stack))

        return result
