class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        right = len(people) - 1
        boat = 0
        while right > left:
            pair_weight = people[left] + people[right]
            if pair_weight > limit:
                right -=1
            elif pair_weight <= limit:
                boat +=1
                left +=1
                right -=1
        boat += (len(people) - 2*boat)
        return boat