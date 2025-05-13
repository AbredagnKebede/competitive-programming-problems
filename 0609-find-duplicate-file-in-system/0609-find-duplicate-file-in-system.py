class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_set = defaultdict(list)
        new = []
        for i in paths:
            single_path = i.split()
            for j in range(1,len(single_path)):
                n = single_path[j].split(".txt")
                new.append([single_path[0]+"/"+n[0]+".txt", n[1]])
        for root, content in new:
            hash_set[content].append(root) 
        ans = []
        for i in hash_set:
            if len(hash_set[i]) > 1:
                ans.append(hash_set[i])
        return ans