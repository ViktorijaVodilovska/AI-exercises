from state_space_search.uninformed_search import *


class MovingObstacles(Problem):
    def __init__(self, man_x, man_y, house_x, house_y):
        self.house_x = house_x
        self.house_y = house_y
        initial = (man_x, man_y, 2, True, 2, 2, True, 2, True)
        super().__init__(initial)

    def move_blocks(self, state):
        man_x, man_y, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down = state
        if block1_x == 0:
            going_left = False
        elif block1_x == 4:
            going_left = True
        if going_left:
            block1_x -= 1
        else:
            block1_x += 1

        if block2_x == 4 and block2_y == 4:
            going_upR = False
        elif block2_x == 0 and block2_y == 0:
            going_upR = True
        if going_upR:
            block2_x += 1
            block2_y += 1
        else:
            block2_x -= 1
            block2_y -= 1

        if block3_y == 0:
            going_down = False
        elif block3_y == 4:
            going_down = True
        if going_down:
            block3_y -= 1
        else:
            block3_y += 1

        return man_x, man_y, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down

    def taken_blocks(self, block1_x, block2_x, block2_y, block3_y):
        return [(block1_x, 8), (block1_x + 1, 8), (block2_x, block2_y), (block2_x + 1, block2_y),
                (block2_x, block2_y + 1), (block2_x + 1, block2_y + 1), (8, block3_y), (8, block3_y + 1)]

    def successor(self, state):
        successors = dict()

        man_x, man_y, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down = self.move_blocks(
            state)
        taken = self.taken_blocks(block1_x, block2_x, block2_y, block3_y)

        if (not ((man_y > 5 and man_x == 5) or (man_y <= 5 and man_x == 10))) and (man_x + 1, man_y) not in taken:
            successors["Desno"] = (
                man_x + 1, man_y, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down)
        if man_x != 0 and (man_x - 1, man_y) not in taken:
            successors["Levo"] = (
                man_x - 1, man_y, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down)
        if not ((man_x <= 5 and man_y == 10) or (man_x > 5 and man_y == 5)) and (man_x, man_y + 1) not in taken:
            successors["Gore"] = (
                man_x, man_y + 1, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down)
        if man_y != 0 and (man_x, man_y - 1) not in taken:
            successors["Dolu"] = (
                man_x, man_y - 1, block1_x, going_left, block2_x, block2_y, going_upR, block3_y, going_down)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.house_x and state[1] == house_y

    def value(self):
        pass


if __name__ == '__main__':
    # Vcituvanje na vleznite argumenti za test primerite
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())
    problem = MovingObstacles(man_x, man_y, house_x, house_y)
    print(breadth_first_graph_search(problem).solution())
