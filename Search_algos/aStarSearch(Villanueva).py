# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:47:28 2022

@author: kylev
"""
def heuristic(n):
    H_dist = {
         'S': 6,
         'A': 4,
         'B': 5,
         'C': 2,
         'D': 2,
         'E': 8,
         'F': 4,
         'G': 0
    }
    return H_dist[n]

Graph_nodes = {
    'S': [('B', 1), ('A', 2), ('F', 3)],
    'B': [('E', 4),('D',2)],
    'A': [('D', 3),('C',2)],
    'F': [('G',6)],
    'E': [],
    'D': [('G',4)],
    'C': [('G',4)],
    'G': []
}


def aStarSearch(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}             
    parents = {}        
    
    g[start_node] = 0

    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
       
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
               
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
              
                else:
                    if g[m] > g[n] + weight:
                        
                        g[m] = g[n] + weight
                       
                        parents[m] = n
                      
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        
  
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
   
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    