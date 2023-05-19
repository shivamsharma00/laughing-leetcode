'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''

def maximalRectangle(matrix):
    r = len(matrix)
    c = len(matrix[0])

    hor_max = [[0] * c for i in range(r)]
    vor_max = [[0] * c for i in range(r)]

    for i in range(r):
        for j in range(r):
            
            if j == 0:
                hor_max[i][j] = int(matrix[i][j])
            else:
                hor_max[i][j] = int(matrix[i][j]+hor_max[i][j-1])
            
            if i == 0:
                vor_max[i][j] = int(matrix[i][j])
            else:
                vor_max[i][j] = int(matrix[i][j] + vor_max[i-1][j])
            
    print(hor_max[i] for i in range(r))
    print(vor_max[i] for i in range(c))
    for i in range(r):
        print(hor_max[i])

    


if __name__ ==  '__main__':
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    maximalRectangle(matrix)