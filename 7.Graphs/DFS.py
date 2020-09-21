'''
Implementation of DFS Algorithm
Reference:https://www.youtube.com/watch?v=FvGCzzfdOLw
'''
def dfs(u):
    visited[u]=True #Grey
    dfs_trav_output.append(u)

    for v in adj_list[u]:
        if visited[v]==False:
            dfs(v)




adj_list={
            "A":["B","C"],
            "B":["A","D","E"],
            "C":["A","F","G"],
            "D":["B"],
            "E":["B"],
            "F":["C"],
            "G":["C"]

          }
visited={}
dfs_trav_output=[]
for node in adj_list.keys():
    visited[node]=False

for u in adj_list.keys():
    if not visited[u]:
        dfs(u)
print(dfs_trav_output)

'''
Example 1:
adj_list={
            "A":["B","C"],
            "B":["D","E"],
            "C":["B","F"],
            "D":[],
            "E":["F"],
            "F":[]
          }
OUTPUT:
['A', 'B', 'D', 'E', 'F', 'C']

Example 2:
adj_list={
            "A":["B"],
            "B":["A","D","E"],
            "C":["F"],
            "D":["B"],
            "E":["B"],
            "F":["C"]
          }
'''