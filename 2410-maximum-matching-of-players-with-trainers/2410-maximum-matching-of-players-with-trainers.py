class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ptrplayer, ptrtrainer, matches = 0, 0, 0
        while ptrplayer < len(players) and ptrtrainer < len(trainers):
            if players[ptrplayer] <= trainers[ptrtrainer]:
                matches +=1
                ptrplayer +=1
            ptrtrainer +=1
        return matches    