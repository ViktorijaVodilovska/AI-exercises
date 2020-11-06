from informed_search import *
from sys import maxsize as infinity


def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


class Pacman(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.obstacles = [[6, 0], [4, 1], [5, 1], [6, 1], [8, 1], [1, 2], [6, 2], [1, 3], [1, 4],
                          [8, 4], [9, 4], [4, 5], [0, 6], [3, 6], [4, 6], [5, 6], [4, 7], [8, 7],
                          [9, 7], [0, 8], [8, 8], [9, 8], [0, 9], [1, 9], [2, 9], [3, 9], [6, 9]]

    def right(self, state):
        x, y, dots = state[0], state[1], list(state[-1])
        if x < 9 and [x + 1, y] not in self.obstacles:
            if (x + 1, y) in dots:
                dots.remove((x + 1, y))
            return [x + 1, y, "istok", tuple(dots)]
        return None

    def left(self, state):
        x, y, dots = state[0], state[1], list(state[-1])
        if x > 0 and [x - 1, y] not in self.obstacles:
            if (x - 1, y) in dots:
                dots.remove((x - 1, y))
            return [x - 1, y, "zapad", tuple(dots)]
        return None

    def up(self, state):
        x, y, dots = state[0], state[1], list(state[-1])
        if y < 9 and [x, y + 1] not in self.obstacles:
            if (x, y + 1) in dots:
                dots.remove((x, y + 1))
            return [x, y + 1, "sever", tuple(dots)]
        return None

    def down(self, state):
        x, y, dots = state[0], state[1], list(state[-1])
        if y > 0 and [x, y - 1] not in self.obstacles:
            if (x, y - 1) in dots:
                dots.remove((x, y - 1))
            return [x, y - 1, "jug", tuple(dots)]
        return None

    def successor(self, state):
        successors = dict()
        pacman_dir = state[2]

        move_right = self.right(state)
        move_left = self.left(state)
        move_up = self.up(state)
        move_down = self.down(state)

        if pacman_dir == "istok":
            if move_right is not None:
                successors["ProdolzhiPravo"] = tuple(move_right)
            if move_left is not None:
                successors["ProdolzhiNazad"] = tuple(move_left)
            if move_up is not None:
                successors["SvrtiLevo"] = tuple(move_up)
            if move_down is not None:
                successors["SvrtiDesno"] = tuple(move_down)
        elif pacman_dir == "zapad":
            if move_left is not None:
                successors["ProdolzhiPravo"] = tuple(move_left)
            if move_right is not None:
                successors["ProdolzhiNazad"] = tuple(move_right)
            if move_down is not None:
                successors["SvrtiLevo"] = tuple(move_down)
            if move_up is not None:
                successors["SvrtiDesno"] = tuple(move_up)
        elif pacman_dir == "sever":
            if move_up is not None:
                successors["ProdolzhiPravo"] = tuple(move_up)
            if move_down is not None:
                successors["ProdolzhiNazad"] = tuple(move_down)
            if move_left is not None:
                successors["SvrtiLevo"] = tuple(move_left)
            if move_right is not None:
                successors["SvrtiDesno"] = tuple(move_right)
        else:
            if move_down is not None:
                successors["ProdolzhiPravo"] = tuple(move_down)
            if move_up is not None:
                successors["ProdolzhiNazad"] = tuple(move_up)
            if move_right is not None:
                successors["SvrtiLevo"] = tuple(move_right)
            if move_left is not None:
                successors["SvrtiDesno"] = tuple(move_left)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0

    def h(self, node):
        pac_x, pac_y = node.state[0], node.state[1]
        max_distance = 0
        for dot in node.state[-1]:
            dist = manhattan((pac_x, pac_y), dot)
            max_distance = max(max_distance, dist)
        return max_distance

    def value(self):
        pass


if __name__ == "__main__":
    pacman_x = int(input())
    pacman_y = int(input())
    direction = input()
    n = int(input())
    positions = []
    for i in range(0, n):
        positions.append(tuple(int(i) for i in input().split(",")))

    pacman = Pacman((pacman_x, pacman_y, direction, tuple(positions)))
    print(astar_search(pacman).solution())
