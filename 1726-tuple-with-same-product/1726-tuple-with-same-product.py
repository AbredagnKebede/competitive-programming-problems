class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pairs = []
        valid_tuples = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pairs.append([nums[i],nums[j]])
        
        pair_products = defaultdict(list)
        for i in pairs:
            pair_products[i[0]*i[1]].append(i)

        for i in pair_products:
            if len(pair_products[i])> 1:
                valid_tuples += (len(list(combinations(pair_products[i],2)))*8)
        
        return valid_tuples 