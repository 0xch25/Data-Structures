'''
Implementation of Undirected Graphs using dict

Reference: https://www.youtube.com/watch?v=QsAUil2eBZs
'''
class Graph:
    def __init__(self,Nodes):
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]=[]

    def print_adj_list(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def degree(self,node):
        return len(self.adj_list[node])


nodes=["A","B","C","D","E"]
all_edges=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]
graph=Graph(nodes)
for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_adj_list()
print(graph.degree("C"))

'''
Output:
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D', 'E']
D -> ['B', 'C', 'E']
E -> ['C', 'D']
3
'''