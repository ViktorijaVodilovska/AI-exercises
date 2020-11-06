from uninformed_search import *


class Circle(Problem):
    def __init__(self, n, s, t, r0, p1, p2, m):
        ar = [r0]
        for i in range(1, n):
            ar.append((ar[i - 1] * p1 + p2) % m)
        self.circle = ar
        self.num = n
        super().__init__(s, t)

    def successor(self, state):
        successors = dict()
        steps = self.circle[state]

        if steps == 0:
            return successors

        for j in range(0, steps):
            i = j+1
            successors["clockwise " + str(i)] = (state + i) % self.num
            successors["counterclockwise " + str(i)] = (state + self.num - i) % self.num

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def value(self):
        pass


if __name__ == "__main__":
    p = Circle(9, 0, 2, 1, 3, 4, 7)
    s = breadth_first_graph_search(p)
    if s is not None:
        print(len(s.solution()))
    else:
        print(-1)
