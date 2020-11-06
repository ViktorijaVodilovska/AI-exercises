from state_space_search.uninformed_search import *

atoms = ["H1", "H2", "O"]


class Molecule(Problem):
    def __init__(self, h1x, h1y, h2x, h2y, ox, oy):
        initial = ((h1x, h1y), (h2x, h2y), (ox, oy))
        self.obstacles = (
            (0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2), (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6),
            (8, 5))
        super().__init__(initial)

    def successor(self, state):
        successors = dict()

        for i, ((x, y), atom) in enumerate(zip(state, atoms)):
            y1 = y + 1
            while y1 < 7 and (x, y1) not in self.obstacles and (x, y1) not in state:
                y1 += 1
            y1 -= 1
            if y1 != y:
                updated = list(state)
                updated[i] = (x, y1)
                successors["Gore" + atom] = tuple(updated)

            y1 = y - 1
            while y1 >= 0 and (x, y1) not in self.obstacles and (x, y1) not in state:
                y1 -= 1
            y1 += 1
            if y1 != y:
                updated = list(state)
                updated[i] = (x, y1)
                successors["Dolu" + atom] = tuple(updated)

            x1 = x - 1
            while x1 >= 0 and (x1, y) not in self.obstacles and (x1, y) not in state:
                x1 -= 1
            x1 += 1
            if x1 != x:
                updated = list(state)
                updated[i] = (x1, y)
                successors["Levo" + atom] = tuple(updated)

            x1 = x + 1
            while x1 < 9 and (x1, y) not in self.obstacles and (x1, y) not in state:
                x1 += 1
            x1 -= 1
            if x1 != x:
                updated = list(state)
                updated[i] = (x1, y)
                successors["Desno" + atom] = tuple(updated)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        (h1x, h1y), (h2x, h2y), (ox, oy) = state
        if h1y == h2y == oy:
            if (h1x - ox) == -1 and (h2x - ox) == 1:
                return True
        return False

    def value(self):
        pass

    # def h(self, node):
    #     ...


if __name__ == '__main__':
    # Vcituvanje na vleznite argumenti za test primerite
    h1_atom_x = int(input())
    h1_atom_y = int(input())
    o_atom_x = int(input())
    o_atom_y = int(input())
    h2_atom_x = int(input())
    h2_atom_y = int(input())
    problem = Molecule(h1_atom_x, h1_atom_y, h2_atom_x, h2_atom_y, o_atom_x, o_atom_y)
    print(breadth_first_graph_search(problem).solution())
