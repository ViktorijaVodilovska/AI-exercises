from constraint import *

boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 4,
         4, 4, 5, 5, 5, 6, 6, 6, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 7, 7, 7, 8, 8, 8, 9, 9, 9, 7, 7,
         7, 8, 8, 8, 9, 9, 9]
rows = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
        5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9,
        9, 9, 9, 9, 9, 9, 9]

if __name__ == '__main__':
    solver = input()
    if solver == "BacktrackingSolver":
        Solver = BacktrackingSolver
    elif solver == "RecursiveBacktrackingSolver":
        Solver = RecursiveBacktrackingSolver
    else:
        Solver = MinConflictsSolver
    problem = Problem(Solver())

    variables = range(0, 81)
    domains = range(1, 10)
    problem.addVariables(variables, domains)

    for i in range(1, 10):
        problem.addConstraint(AllDifferentConstraint(), [n for n in variables if boxes[n] == i])
    for i in range(1, 10):
        problem.addConstraint(AllDifferentConstraint(), [n for n in variables if rows[n] == i])
    for i in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), [n for n in variables if n % 9 == i])

    print(problem.getSolution())
