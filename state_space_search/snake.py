from state_space_search.uninformed_search import *

labels = ["ProdolzhiPravo", "SvrtiLevo", "SvrtiDesno"]

dir_dict = {
    "N": [0, 3, 2],
    "S": [1, 2, 3],
    "W": [3, 1, 0],
    "E": [2, 0, 1]
}


def allmoves(pos, direction):
    x, y = pos
    res = []
    for i in dir_dict[direction]:
        if i == 0:
            res.append((x, y + 1, "N"))
        if i == 1:
            res.append((x, y - 1, "S"))
        if i == 2:
            res.append((x + 1, y, "E"))
        if i == 3:
            res.append((x - 1, y, "W"))
    return res


class Snake(Problem):
    def __init__(self, green, red):
        # green, direction of facing, head position, body positions
        initial = (green, "S", (0, 7), ((0, 8), (0, 9)))
        self.red = red
        super().__init__(initial)


    def body(self, head, body, eat):
        moved = [head]
        for i in range(len(body) - 1):
            moved.append(body[i])
        if eat:
            moved.append(body[-1])
        return tuple(moved)

    def successor(self, state):
        successors = dict()

        not_eaten, direction, head, body = state

        moves = allmoves(head, direction)

        for i, pos in enumerate(moves):
            x, y, d = pos
            if x != -1 and y != -1 and x <= 9 and y <= 9 and (x, y) not in self.red:
                apples = list(not_eaten)
                eat = False
                if (x, y) in not_eaten:
                    apples.remove((x, y))
                    eat = True
                new_body = self.body(head, body, eat)
                if (x,y) not in new_body:
                    successors[labels[i]] = (tuple(apples), d, (x, y), new_body)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[0]) == 0

    def value(self):
        pass


if __name__ == '__main__':
    n = int(input())
    zeleni_jabolki = [tuple(map(int, input().split(','))) for _ in range(n)]
    m = int(input())
    crveni_jabolki = [tuple(map(int, input().split(','))) for _ in range(m)]
    problem = Snake(tuple(zeleni_jabolki),tuple(crveni_jabolki))
    print(breadth_first_graph_search(problem).solution())
