class Solution:
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1  
            else:
                return 0   

        nums_str.sort(key=cmp_to_key(compare))

        largest_num = ''.join(nums_str)

        if largest_num[0] == '0':
            return '0'
        print(sorted(["3", "30"]) )
        return largest_num
