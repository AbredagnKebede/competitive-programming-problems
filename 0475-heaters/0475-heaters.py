class Solution:
    def findRadius(self, houses, heaters):
        
        houses=sorted(houses)
        heaters=sorted(heaters)
        
        heaters = heaters + [float('inf')]
        i1,i2,r = 0,1,0

        for h in houses:
            while h >= heaters[i2]:
                i1,i2 = i2,i1+1
            r = max(r,min(abs(h - heaters[i1]),heaters[i2] - h))            
        return r