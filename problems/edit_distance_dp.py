'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.



    h  o  r  s  e
r   0  0  -1 1  0
o   0  -1  0 1  0
s   0  0  0  -1  0 


    i  n  t  e  n  t  i  o  n
e   0  0  0  1  0  0  0  0  0
x   0  7  4  1  7  
e
c
u
t
i
o
n
    r o s
    3 2 4

    h o r s e
    0 0 0 0 0
    0 1 1 1 0


    e x e c u t i o n

    3 0 3 0 0


    1 0 0 0 0 0 1 2 3 
    i n t e n t i o n
    i n e n t i o n
    
    e n e n t i o n 

    e x e n t i o n


    h  o  r  s  e
    0  2  1  3  0

    r o s


    i  n  t  e  n  t  i  o  n
e   7  9  6  1  9  6  7  8  9




x     0  0  0  0  0  0  0  0
e   
c
u
t
i
o
n
'''

def minDistance(word1, word2):
    
    w1 = int(len(word1))+1
    w2 = int(len(word2))+1

    m1 = [[0] * (w1) for _ in range(0, w2)]

    for j in range(0, w1):
        m1[0][j] = j
    for i in range(0, w2):
        m1[i][0] = i

    for i in range(1, w2):
        for j in range(1, w1):
            replace_cost = 0 if word1[j-1] == word2[i-1] else 1
            m1[i][j] = min(m1[i-1][j]+1, m1[i][j-1]+1, m1[i-1][j-1]+replace_cost)
    return m1[w2-1][w1-1]

    

if __name__ == '__main__':
    print(minDistance('horse', 'ros'))
    print(minDistance('intention', 'execution'))