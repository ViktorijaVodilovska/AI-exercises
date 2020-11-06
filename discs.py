from informed_search import *


class Discs(Problem):
    def __init__(self, num, arr_len):
        initial = tuple([i if i <= n else 0 for i in range(1, arr_len + 1)])
        goal = tuple([i if i <= n else 0 for i in range(arr_len, 0, -1)])
        super().__init__(initial, goal)
        self.length = arr_len
        self.n = num

    def successor(self, state):
        successors = dict()

        for i in range(0, self.length):
            x = state[i]
            if x != 0:
                array = list(state)
                if i != self.length - 1:
                    if array[i + 1] == 0:
                        array[i], array[i + 1] = array[i + 1], array[i]
                        successors["D1: Disk " + str(x)] = tuple(array)
                        array = list(state)
                    elif i < self.length - 2:
                        if array[i + 2] == 0:
                            array[i], array[i + 2] = array[i + 2], array[i]
                            successors["D2: Disk " + str(x)] = tuple(array)
                            array = list(state)
                if i != 0:
                    if array[i - 1] == 0:
                        array[i], array[i - 1] = array[i - 1], array[i]
                        successors["L1: Disk " + str(x)] = tuple(array)
                    elif i > 1:
                        if array[i - 2] == 0:
                            array[i], array[i - 2] = array[i - 2], array[i]
                            successors["L2: Disk " + str(x)] = tuple(array)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def value(self):
        pass

    def h(self, node):
        count = 0
        for x, y in zip(node.state, self.goal):
            if x != y and x != 0:
                count += 1
        return count


if __name__ == "__main__":
    n = int(input())
    l = int(input())
    discs = Discs(n, l)
    print(astar_search(discs).solution())
