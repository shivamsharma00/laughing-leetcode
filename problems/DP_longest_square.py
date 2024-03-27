'''
1139. Largest 1-Bordered Square
Medium

541

86

Add to List

Share
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1

'''

def largest1BorderedSquare(grid):
        
        rowlen = int(len(grid))
        collen = int(len(grid[0]))
        # print(rowlen, collen)

        horlist = [[0]*collen for i in range(rowlen)]
        vorlist = [[0]*collen for j in range(rowlen)]
        
        # horlist[0][0], vorlist[0][0] = grid[0][0]
        for i in range(collen):
            vorlist[0][i] = grid[0][i]
        for j in range(rowlen):
            horlist[j][0] = grid[j][0]
        # for i in range(len(vorlist)):
        #     print(vorlist[i])
        for i in range(0, rowlen):
            for j in range(0, collen):
                if grid[i][j] == 1:
                    horlist[i][j] = horlist[i][j-1] + 1
                    # if j == 0:
                        # vorlist[i][j] = vorlist[i-1][j] + 1
                    if i > 0 :
                        vorlist[i][j] = vorlist[i-1][j] + 1
                else:
                    horlist[i][j] = 0
                    vorlist[i][j] = 0
            
            
        for i in range(len(horlist)):
            print(horlist[i])
        print('\n')
        for i in range(len(vorlist)):
            print(vorlist[i])
        # print(horlist)
        # print(vorlist)
        max = 0
        for i in range(rowlen-1, -1, -1):
            for j in range(collen-1, -1, -1):
                small = min(horlist[i][j], vorlist[i][j])
                
                while small > max:
                    if (horlist[i-small+1][j]>=small) and (vorlist[i][j-small+1] >= small):
                        max = small
                    small -=1
        return max**2





# grid = [[1, 1, 0, 1]]
grid = [[1, 0, 1, 1], 
        [1, 0, 0, 1], 
        [1, 0, 0, 1], 
        [1, 1, 1, 1]]
# grid = [[1, 1, 0, 0]]
print(largest1BorderedSquare(grid))        
                    
                
                