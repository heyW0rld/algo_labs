from typing import MutableSet


def kruskal(adj_matrix):
    inc_matrix = adj_to_inc(adj_matrix)
    inc_matrix.sort(key=lambda item: item[2])

    cost = 0
    visited = [False] * len(adj_matrix)

    for node in inc_matrix:
        if not visited[node[0]] or not visited[node[1]]:
            cost += node[2]
            visited[node[0]] = True
            visited[node[1]] = True

            print(f'{str(node[0])}-{str(node[1])}:{str(node[2])}')

    print(f'min cost: {cost}')


def adj_to_inc(matrix):
    res = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                res.append([i, j, matrix[i][j]])

    return res


if __name__ == '__main__':
    matrix = [
        [0, 4, 0, 3, 5],
        [4, 0, 2, 0, 0],
        [0, 2, 0, 1, 0],
        [3, 0, 1, 0, 0],
        [5, 0, 0, 0, 0]
    ]

    kruskal(matrix)