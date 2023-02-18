# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:39:54 2022

@author: kylev
"""
import sys


graph = {
  'S' : ['B','A', 'F'],
  'B' : ['E', 'D'],
  'A' : ['D', 'C'],
  'F' : ['G'],
  'E' : [],
  'D' : ['G'],
  'C' : ['G'],
  'G' : []
}


visited = set() 
list = list()
def dfs(visited, graph, node):  
    if node not in visited:
        list.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            if neighbour == 'G':
             print(list)
             sys.exit()
                    


print("Following is the Depth-First Search")
dfs(visited, graph, 'S')