
class Graph:
  
  def __init__(self,n):
    self.nodes = {}
    self.distances = {}
    for i in range(1,n+1):
      self.nodes[i] = []

  
  def connect(self, x,y):
    self.nodes.get(y).append(x)
    self.nodes.get(x).append(y)
    
  def find_all_distances(self, s):
    fronteir = self.nodes[s]
    depth = 1
    explored = set()
    to_be_explored = set(self.nodes[s])
    nodes_explored = 0
    nodes_before_next_level = len(fronteir)
    while fronteir:
      # print(fronteir)
      node = fronteir[0]
      self.distances[node] = depth *6
      explored.add(node)
      nodes_explored += 1
      for child in self.nodes[node]:
        if child not in explored and child not in to_be_explored:
          to_be_explored.add(child)
          fronteir.append(child)
      fronteir.remove(node)
      if nodes_explored == nodes_before_next_level:
        depth += 1
        nodes_before_next_level = len(fronteir)
        nodes_explored = 0
      
      
      
    for node in self.nodes:
      if node not in self.distances:
        self.distances[node] = -1
    
    answer = []
    for node in self.distances:
      if node != s:
        a = self.distances[node]
        answer.append(str(a))
    print(' '.join(answer))
  
fileInput = open('input06.txt')

# t = int(input())
t = int(fileInput.readline())
for i in range(t):
    n,m = [int(value) for value in fileInput.readline().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in fileInput.readline().split()]
        graph.connect(x,y)
    s = int(fileInput.readline())
    graph.find_all_distances(s)