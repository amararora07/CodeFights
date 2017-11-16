def dfsComponentSize(matrix, vertex):

    def dfs(currentVertex, visited):
        return matrix[vertex].count(True)+1

    visited = []

    for i in range(len(matrix)):
        visited.append(False)

    componentSize = dfs(vertex, visited)

    return componentSize
