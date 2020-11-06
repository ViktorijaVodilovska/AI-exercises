from uninformed_search import *


class Hanoj(Problem):
    def __init__(self, initial, goal):
        self.n = len(initial_towers)
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        pillars = [list(i) for i in state]

        for i in range(self.n):
            if pillars[i]:
                for j in range(self.n):
                    if not pillars[j]:
                        pillars[j].append(pillars[i].pop())
                        successors["MOVE TOP BLOCK FROM PILLAR " + str(i+1) + " TO PILLAR " + str(j+1)] = tuple(
                            [tuple(p) for p in pillars])
                        pillars = [list(k) for k in state]
                    elif pillars[i][-1] <= pillars[j][-1]:
                        pillars[j].append(pillars[i].pop())
                        successors["MOVE TOP BLOCK FROM PILLAR " + str(i+1) + " TO PILLAR " + str(j+1)] = tuple(
                            [tuple(p) for p in pillars])
                        pillars = [list(k) for k in state]
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
    s = input()
    initial_towers = tuple([tuple(map(int, x.split(','))) if x != '' else () for x in s.split(';')])
    s = input()
    goal_towers = tuple([tuple(map(int, x.split(','))) if x != '' else () for x in s.split(';')])
    problem = Hanoj(initial_towers, goal_towers)
    solution = breadth_first_graph_search(problem).solution()
    print("Number of steps required: " + str(len(solution)))
    print("Solution:")
    for i in solution:
        print(i)