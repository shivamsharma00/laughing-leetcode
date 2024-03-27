'''
48. Rotate Image
Medium

10365

528

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
[
    [ 0,0 , 0,1 , 0,2 , 0,3 ],
    [ 1,0 , 1,1 , 1,2 , 1,3 ],
    [ 2,0 , 2,1 , 2,2 , 2,3 ],
    [ 3,0 , 3,1 , 3,2 , 3,3 ],
]

[
    [ 3,0 , 2,0 ,  1,0 , 0,0 ],
    [ 3,1 , 2,1 , 1,1 , 0,1 ],
    [ 3,2 , 2,2 , 1,2 , 0,2 ],
    [ 3,3 , 2,3 , 1,3 , 0,3 ],    
]

1 - 1, 0
2 - 1, 1
3 - 2, 2 
4 - 2, 3
5 - 3
6 - 3 
7 - 4 
8 - 4
int(a/2) if a%2==0 else int(a/2)+1



Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print()
    # print(matrix)

    for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
            
    return matrix

def rotate1(matrix):
       # step 1: transpose in-place
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(i, columns):
                # swap
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        # step 2 - swap row-wise elements
        for i in range(rows):
            for j in range(columns // 2):
                # swap
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][columns - j - 1]
                matrix[i][columns - j - 1] = tmp
        return matrix

if __name__== '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    for i in m:
        print(i)
    for i in rotate(m):
        print(i)
    print()
    for i in rotate1(m):
        print(i)
