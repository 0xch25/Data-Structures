'''
Implementation of Topological Sorting
References: https://www.interviewcake.com/concept/python3/topological-sort
'''
def topological_sort(digraph):
    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for neighbor in digraph[node]:
            indegrees[neighbor] += 1


    nodes_with_no_incoming_edges = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)


    topological_ordering = []
    while len(nodes_with_no_incoming_edges) > 0:
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)
        for neighbor in digraph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_incoming_edges.append(neighbor)
    if len(topological_ordering) == len(digraph):
        return topological_ordering
    else:
        raise Exception("Graph has a cycle! No topological ordering exists.")

digraph={
            "1":["2","3"],
            "2":["4","5"],
            "3":["4"],
            "4":["5"],
            "5":[]
          }
print(topological_sort(digraph))