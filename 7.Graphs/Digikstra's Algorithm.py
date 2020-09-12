'''
 Dijkstra's algorithm for Weighted Directed Graph
 References: https://www.youtube.com/watch?v=Rb0xjNAk5qI
'''
import heapq
from collections import defaultdict


def shortestPath(graph, src, dest):
    h = []
    # keep a track record of vertices with the cost
    # heappop will return vertex with least cost
    # greedy SRC -> MIN - > MIN -> MIN -> DEST

    heapq.heappush(h, (0, src))

    while len(h) != 0:
        currcost, currvtx = heapq.heappop(h)
        if currvtx == dest:
            print("Path Exisits {} to {} with cost {}".format(src, dest, currcost))
            break
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(h, (currcost + neighcost, neigh))


graph = defaultdict(list)
print("Enter the number of vertecis:")
v, e = map(int, input().split())
print("enter the edges:")
for i in range(e):
    u, v, w = map(str, input().split())
    graph[u].append((v, int(w)))
print("enter the src and edges:")
src, dest = map(str, input().split())
shortestPath(graph, src, dest)

'''
INPUT:
Enter the number of vertecis:
6 7
enter the edges:
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
enter the src and edges:
A D
OUTPUT:
Path Exisits A to D with cost 9
'''