from constraint import *


def knights_attacking(n1, n2):
    if (abs(n1[0] - n2[0]), abs(n1[1] - n2[1])) in [(1, 2), (2, 1)] or n1 == n2:
        return False
    return True


if __name__ == '__main__':
    n = int(input())
    problem = Problem()

    variables = range(n)
    domains = []
    for i in range(n):
        for j in range(n):
            domains.append((i, j))
    problem.addVariables(variables, domains)

    for knight1 in variables:
        for knight2 in variables:
            if knight1 != knight2:
                problem.addConstraint(lambda n1, n2: knights_attacking(n1, n2), (knight1, knight2))

    if n <= 4:
        solution = problem.getSolutions()
        print(len(solution))
    else:
        print(problem.getSolution())
