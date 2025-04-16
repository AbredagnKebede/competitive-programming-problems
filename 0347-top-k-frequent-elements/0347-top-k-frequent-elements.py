class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        #sort the above dic based on their values
        ans = [] 
        sorted_in_value = sorted(count_nums.items(), key = lambda item: item[1], reverse = True)
        for i in sorted_in_value:
            if k > 0:
                ans.append(i[0])
            else:
                break
            k -=1
        return ans

