def prim(adj_matrix):
    no_edge = 0
    n = len(adj_matrix)

    visited = [False] * n
    visited[0] = True

    cost = 0

    while no_edge < n - 1:
        minimum = 999
        a = 0
        b = 0

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and adj_matrix[i][j]:
                        if minimum > adj_matrix[i][j]:
                            minimum = adj_matrix[i][j]
                            a = i
                            b = j

        print(f'{str(a)}-{str(b)}:{str(adj_matrix[a][b])}')
        cost += adj_matrix[a][b]
        visited[b] = True
        no_edge += 1
    print(f'min cost: {cost}')


if __name__ == '__main__':
    matrix = [
        [0, 4, 0, 3, 5],
        [4, 0, 2, 0, 0],
        [0, 2, 0, 1, 0],
        [3, 0, 1, 0, 0],
        [5, 0, 0, 0, 0]
    ]

    prim(matrix)