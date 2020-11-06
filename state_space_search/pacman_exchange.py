from state_space_search.informed_search import *


class Exchange(Problem):
    def __init__(self, m, n):
        self.N = n
        self.M = m
        yellow = []
        green = []

        # (x,y) tuple for the location of a pacman in the grid: x-column, y-row

        # yellow in leftmost column -> (0, y) | y e [m/2, m)
        for i in range(m // 2, m):
            yellow.append((0, i))

        # green in rightmost column -> (n-1, y) | y e [0, m/2)
        for i in range(0, m // 2):
            green.append((n - 1, i))

        super().__init__((tuple(yellow), tuple(green)), (tuple(green), tuple(yellow)))

    def successor(self, state):
        successors = dict()
        all_pacmans = []
        for i, j in zip(state[0], state[1]):
            all_pacmans.append(i)
            all_pacmans.append(j)

        # move all yellow ones in all possible directions
        for i in range(0, self.M // 2):
            # move right
            yellow = list(state[0])
            x, y = yellow[i]
            while x != self.N - 1:
                x += 1
                if (x, y) in all_pacmans:
                    break
                yellow[i] = (x, y)
                successors["Y" + str(i) + " " + str((x, y))] = (tuple(yellow), state[1])

            # move down
            yellow = list(state[0])
            x, y = yellow[i]
            while y != 0:
                y -= 1
                if (x, y) in all_pacmans:
                    break
                yellow[i] = (x, y)
                successors["Y" + str(i) + " " + str((x, y))] = (tuple(yellow), state[1])

        # move all green ones in all possible directions
        for i in range(0, self.M // 2):
            # move left
            green = list(state[1])
            x, y = green[i]
            while x != 0:
                x -= 1
                if (x, y) in all_pacmans:
                    break
                green[i] = (x, y)
                successors["G" + str(i) + " " + str((x, y))] = (state[0], tuple(green))

            # move up
            green = list(state[1])
            x, y = green[i]
            while y != self.M - 1:
                y += 1
                if (x, y) in all_pacmans:
                    break
                green[i] = (x, y)
                successors["G" + str(i) + " " + str((x, y))] = (state[0], tuple(green))

        return successors

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def value(self):
        pass

    def h(self, node):
        num = 0
        for st, g in zip(node.state, self.goal):
            for pos, g_pos in zip(st, g):
                x, y = pos
                x_g, y_g = g_pos
                if x != x_g:
                    num += 1
                if y != y_g:
                    num += 1
        return num


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    problem = Exchange(m, n)
    # print(breadth_first_graph_search(problem).solution())
    print(astar_search(problem).solution())
