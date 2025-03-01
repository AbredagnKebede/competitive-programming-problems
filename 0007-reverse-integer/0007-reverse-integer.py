class Solution(object):
    def reverse(self, x):
        temp_str = str(x)
        if len(temp_str) == 1:
            return x
        if x > 0: temp_int = int(temp_str[::-1]) 
        else: temp_int = (-1)* int(temp_str[::-1][:-1])
        if temp_int >= -2147483648 and temp_int <= 2147483648:
            return temp_int 
        return 0
        

        