"""
Implementation of BFS Algorithm
Reference:https://www.youtube.com/watch?v=y52hH_TE9qQ
          https://www.youtube.com/watch?v=PQhMkmhYZjQ
"""
from queue import Queue

adj_list={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}
visited={}
level={}
parent={}
bfs_trav_output=[]
queue=Queue()
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
s="A"
visited[s]=True
level[s]=0
queue.put(s)
while not queue.empty():
    u=queue.get()
    bfs_trav_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(bfs_trav_output)
#shortest path from vertex(only if graph is connected):
v="G"
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print("The shortest path is:")
print(path)

'''
OUTPUT:
['A', 'B', 'D', 'C', 'E', 'F', 'G', 'H']
The shortest path is:
['A', 'D', 'E', 'G']

'''