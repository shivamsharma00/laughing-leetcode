'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
'''

# Easy
def isPathCrossing(path: str) -> bool:
    x = 0
    y = 0
    flag = False
    seen = [(0, 0)]
    for p in path[0]:
        print(p)
        if p == 'N':
            x +=1
        elif p == 'S':
            if x == 0:
                x = -1
            else:
                x = x-1
        elif p == 'E':
            y +=1
        elif p == 'W':
            if y == 0:
                y = -1
            else:
                y = y -1
        print(f"x-{x} , y-{y}")
        if (x, y) in seen:
            flag = True
        else:
            seen.append((x, y))
        # if x == 0 and y == 0:
            # flag = True
    return flag

p = ["NNSWWEWSSESSWENNW"]
p2 = ["NESWW"]
print(isPathCrossing(p))
