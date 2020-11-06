from state_space_search.uninformed_search import *


class Black_White(Problem):
    def __init__(self, n, fields):
        self.n = n
        initial = tuple([tuple([fields[i * n + j] for j in range(n)]) for i in range(n)])
        goal = tuple([tuple([1 for j in range(n)]) for i in range(n)])
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        n = self.n
        for i in range(n):
            for j in range(n):
                clicked = list(state)
                clicked = [list(i) for i in clicked]
                clicked[i][j] = abs(clicked[i][j] - 1)
                if i != 0:
                    clicked[i - 1][j] = abs(clicked[i - 1][j] - 1)
                if i != n - 1:
                    clicked[i + 1][j] = abs(clicked[i + 1][j] - 1)
                if j != 0:
                    clicked[i][j - 1] = abs(clicked[i][j - 1] - 1)
                if j != n - 1:
                    clicked[i][j + 1] = abs(clicked[i][j + 1] - 1)
                successors["x: " + str(i) + ", y: " + str(j)] = tuple([tuple(i) for i in clicked])
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def value(self):
        pass


if __name__ == '__main__':
    # vcituvanje na vleznite argumenti za test primerite
    n = int(input())
    fields = list(map(int, input().split(',')))
    problem = Black_White(n, fields)
    print(breadth_first_graph_search(problem).solution())