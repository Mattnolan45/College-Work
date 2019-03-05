import sys
 
class Player(object):
    disqualified_score = -1

    
    def __init__(self, name, handicap, strokes):
        self.name = name
        self.handicap = int(handicap)
        self.strokes = strokes
 
    def handicaps(self, indexes):
        for i in range(0, self.handicap):
            if self.strokes[indexes[i % 18]].isnumeric():
                self.strokes[indexes[i % 18]] = str(int(self.strokes[indexes[i % 18]]) - 1)

    def score(self, pars, indexes):
        score = 0
        for i in range(0, len(self.strokes)):
            if self.strokes[i].isnumeric() and (int(self.strokes[i]) - int(pars[i])) < 2:
                score += 2 - (int(self.strokes[i]) - int(pars[i]))

            elif self.strokes[i] != 'X' and not self.strokes[i].isnumeric():
                score = Player.disqualified_score
                Player.disqualified_score -= 1
                break

        return score
 
 
def main():
    pars = sys.stdin.readline().split()
    index_l = [int(c) for c in sys.stdin.readline().split()]
    indexes = [int(index_l.index(i)) for i in sorted(index_l)]

    player_list = [p.strip().split() for p in sys.stdin.readlines()]
    players = [Player(' '.join(p[:-19]), p[-19], p[-18:]) for p in player_list]
            
 
    longest_name = max([len(player.name) for player in players])


    player_dict = {}
    for player in players:
        player.handicaps(indexes)
        total = player.score(pars, indexes)

        player_dict[player.name] = total
    
    for player in sorted(player_dict, key=lambda x: player_dict[x], reverse=True):
        print("{:>{}} : {:>{}}".format(player, longest_name, 'Disqualified' if player_dict[player] < 0 else player_dict[player], 2))
        

main()