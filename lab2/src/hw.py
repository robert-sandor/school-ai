import cProfile


# greedy best-first search
def find_partition_gbfs(init_list):
    list_a = []
    list_b = []
    for n in sorted(init_list, reverse=True):
        if sum(list_a) < sum(list_b):
            list_a.append(n)
        else:
            list_b.append(n)
    return list_a, list_b


def find_partition_dfs(init_graph, start):
    if graph is None or start is None:
        return [], []

    list_a = []
    list_b = []

    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if sum(list_a) < sum(list_b):
                list_a.append(vertex)
            else:
                list_b.append(vertex)
            if vertex in graph.keys():
                stack += reversed(graph[vertex])

    return list_a, list_b


def input_array():
    array = []
    i = int(input(" > "))
    while i is not 0:
        array.append(i)
        i = int(input(" > "))
    return array


if __name__ == '__main__':
    ms = []
    assert find_partition_gbfs(ms) == ([], [])
    ms = [1]
    assert find_partition_gbfs(ms) == ([], [1])
    ms = [1, 1, 1, 1]
    assert find_partition_gbfs(ms) == ([1, 1], [1, 1])
    ms = [2, 3, 4, 5]
    assert find_partition_gbfs(ms) == ([4, 3], [5, 2])
    ms = [2, 3, 4, 5, 6, 7]
    assert find_partition_gbfs(ms) == ([6, 5, 2], [7, 4, 3])

    ms = input_array()

    # ms = range(1, 1000)
    child1, child2 = find_partition_gbfs(ms)
    print(sum(child1), child1)
    print(sum(child2), child2)
    print("Difference : ", abs(sum(child1) - sum(child2)))
    cProfile.run('find_partition_gbfs(ms)')

    graph = {1: [2, 3],
             2: [4, 5],
             3: [6, 7]}
    assert find_partition_dfs({}) == ([], [])
    assert find_partition_dfs(ms) == ([], [1])
    assert find_partition_dfs(ms) == ([1, 1], [1, 1])
    assert find_partition_dfs(ms) == ([4, 3], [5, 2])
    assert find_partition_dfs(ms) == ([6, 5, 2], [7, 4, 3])
