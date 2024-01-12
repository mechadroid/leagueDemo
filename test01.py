from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
     
    def player_rank(self, rank):
        limit = len(self.standings.items())
        if rank<1:
            return "Please enter a positive Number not greater than "+str(limit)
        if rank > limit:
            return "Please enter a positive Number that is not greater than "+str(limit)
        rank = rank - 1
        # create an iterable object
        LeagueData = []
        # prepare data for sorting
        for player,keyData in self.standings.items():
            dummyData=[]
            dummyData.append(player)
            dummyData.append(keyData['score'])
            dummyData.append(keyData['games_played'])
            LeagueData.append(dummyData)

        ranking = sorted(LeagueData,key=lambda score: (score[1],score[2]))
        return ranking[rank][0]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))