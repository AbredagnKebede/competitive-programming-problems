class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = len(citations)
        for i in citations:
            if i < h:
                h -= 1       
        return h