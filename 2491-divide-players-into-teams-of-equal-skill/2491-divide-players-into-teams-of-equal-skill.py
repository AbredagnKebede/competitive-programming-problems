class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        left = 0
        right = len(skill) - 1
        chemistry = 0
        sum_equal = skill[left] + skill[right]
        while right > left:
            if (skill[left] + skill[right]) != sum_equal:
                return -1
            chemistry += (skill[left]* skill[right])
            right -=1
            left +=1
        return chemistry

