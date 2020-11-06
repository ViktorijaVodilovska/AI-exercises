from constraint import *


def queens_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]):
        return False
    return True


if __name__ == '__main__':

    problem = Problem()

    n = int(input())

    variables = range(1, n+1)
    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))

    problem.addVariables(variables, domains)

    problem.addConstraint()

    for queen1 in variables:
        for queen2 in variables:
            if queen1 != queen2:
                problem.addConstraint(lambda q1,q2: queens_attacking(q1,q2), (queen1, queen2))

    if n <= 6:
        solution = problem.getSolutions()
        print(len(solution))
    else:
        print(problem.getSolution())