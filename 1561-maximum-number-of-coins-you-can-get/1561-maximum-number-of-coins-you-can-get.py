class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        pile_sum = 0
        alice, you, bob = len(piles)-1, len(piles)-2, 0

        while bob < you:
            pile_sum += piles[you]
            alice -= 2
            you -= 2
            bob += 1
        return pile_sum