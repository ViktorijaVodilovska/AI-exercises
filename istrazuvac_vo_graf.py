import math
from informed_search import *

moves = ["Gore", "Dolu", "Levo", "Desno", "DoluDesno", "GoreLevo"]

def coordinates(num):
    num = num-1
    return num/4, num%4

class Explorer(Problem):
    def __init__(self, player, star1, star2):
        stars = (star1,star2)
        graph = ((0, 5, 0, 2, 0, 0), (0, 6, 1, 0, 0, 0), (0, 7, 0, 4, 0, 0), (0, 8, 3, 0, 0, 0),
                 (1, 0, 0, 6, 0, 0), (2, 10, 5, 7, 11, 0), (3, 11, 6, 8, 0, 0), (4, 0, 7, 0, 0, 0),
                 (0, 13, 0, 10, 0, 0), (6, 14, 9, 11, 0, 0), (7, 15, 10, 12, 0, 6), (0, 16, 11, 0, 0, 0),
                 (9, 0, 0, 14, 0, 0), (10, 0, 13, 0, 0, 0), (11, 0, 0, 16, 0, 0), (12, 0, 15, 0, 0, 0))
        initial = (player, stars, graph)
        super().__init__(initial)

    def successor(self, state):
        successors = dict()

        player, stars, graph = state

        for num,z in enumerate(zip(graph[player-1], moves)):
            i, label = z
            if i != 0:
                stars_update = list(stars)
                if i in stars:
                    stars_update.remove(i)
                graph_update = list([list(g) for g in graph])
                graph_update[player-1][num] = 0
                graph_update[i-1][graph_update[i-1].index(player)] = 0
                graph_update = tuple([tuple(g) for g in graph_update])
                successors[label] = (i, tuple(stars_update), graph_update)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

    def value(self):
        pass

    def h(self, node):
        player, stars, g = node.state
        px,py = coordinates(player)
        dist = 0
        for i in stars:
            sx,sy = coordinates(i)
            d = math.sqrt((px-sx)*(px-sx)+(py-sy)*(py-sy))
            if d>dist:
                dist = d
        return dist


if __name__ == '__main__':
    # Vcituvanje na vleznite argumenti za test primerite
    player_position = int(input())
    star_one_position = int(input())
    star_two_position = int(input())
    problem = Explorer(player_position,star_one_position,star_two_position)
    print(astar_search(problem).solution())
