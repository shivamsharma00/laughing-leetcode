'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, 
which has some apples in their vertices. You spend 1 second to walk over 
one edge of the tree. Return the minimum time in seconds you have to spend 
to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, 
where edges[i] = [ai, bi] means that exists an edge connecting 
the vertices ai and bi. Additionally, there is a boolean array hasApple, 
where hasApple[i] = true means that vertex i has an apple; otherwise, 
it does not have any apple.
'''
from collections import defaultdict

def minTime(n, edge, hasApple):
    
    edge_w = [0]*n
    tree = defaultdict(list)
    
    for i in range(n-1):
        
        x, y = edge[i]
        
        tree[x].append(y)
        tree[y].append(x)

        edge_w[y] = edge_w[x] + 1

    print(tree)

    


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
print(minTime(n, edges, hasApple))