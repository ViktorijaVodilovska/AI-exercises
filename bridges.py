from constraint import *

# each of the islands' bridge count
values = [3, 4, 1, 3, 5, 1, 4, 2, 5, 2, 2]
# list for each island of islands its connected to
adj_list = [[1, 2], [0, 4], [0, 3, 7], [2, 4, 8], [1, 3, 6], [6], [4, 5, 10], [2, 8], [3, 7, 9], [8], [6]]
# all the possible connections
# THESE ARE TECHNICALLY THE VARIABLES, TO WHICH WE WILL ASSIGN VALUES
connections = [(0, 1), (0, 2), (1, 4), (2, 3), (2, 7), (3, 4), (3, 8),
               (4, 6), (5, 6), (6, 10), (7, 8), (8, 9)]

# for the path from each to each check:
V = len(values)
B = len(connections)
INFINITY = 99999


# def floyd_warshall(*all_values):
#     dist = [[0 if p == j else INFINITY for j in range(V)] for p in range(V)]
#     for ind in range(B):
#         p, j = connections[ind]
#         w = all_values[ind]
#         if w != 0:
#             dist[p][j] = w
#             dist[p][j] = w
#     for k in range(V):
#         for p in range(V):
#             for j in range(V):
#                 dist[p][j] = min(dist[p][j], dist[p][k] + dist[k][j])
#     for row in dist:
#         if row.__contains__(INFINITY):
#             return False
#     return True


if __name__ == '__main__':

    problem = Problem()
    variables = range(B)
    domains = range(0, 6)  # maximum bridge count is 5
    problem.addVariables(variables, domains)

    for i in range(V):
        bridges = [connections.index((min(i, j), max(j, i))) for j in adj_list[i]]
        problem.addConstraint(MinSumConstraint(values[i]), bridges)
        problem.addConstraint(MaxSumConstraint(values[i]), bridges)

    # problem.addConstraint(floyd_warshall, variables)
    print(problem.getSolution())
