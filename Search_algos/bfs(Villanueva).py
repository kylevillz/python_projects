# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:39:57 2022

@author: kylev
"""

g = {
  'S' : ['B','A', 'F'],
  'B' : ['E', 'D'],
  'A' : ['D', 'C'],
  'F' : ['G'],
  'E' : [],
  'D' : ['G'],
  'C' : ['G'],
  'G' : []
}

queue = []
visited = [] 
list = list()

def bfs(visited, g, node):
  visited.append(node)
  queue.append(node)
  print("BFS TRAVERSAL:")

  while queue:
    s = queue.pop(0) 
    print (s, end = " -> ") 

    for neighbour in g[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, g, 'S')