from queue import Queue

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}


queue = Queue()
visited = {}
levels = {}
parents = {}
bfs_traversal_output = []

for node in graph.keys():
  visited[node] = False
  levels[node] = -1
  parents[node] = None

#Initialize the head of the graph
first_node = "A"
visited[first_node] = True
levels[first_node] = 0
queue.put(first_node)

while not queue.empty():
  u = queue.get()
  bfs_traversal_output.append(u)

  for child in graph[u]:
    if visited[child] == False:
      visited[child] = True
      levels[child] = levels[u]+1
      parents[child] = u 
      queue.put(child)

print(bfs_traversal_output)

print(levels)

#Distance of any node from the source node.
print("Distance from root node A to node F: ", levels["F"])


# Shortest path of any node from source node.
target_node = t = "F"

shortest_path = []

while target_node is not None:
  shortest_path.append(target_node)
  target_node = parents[target_node]

shortest_path.reverse()
print(f"Shortest path to reach `{t}` is:",shortest_path)