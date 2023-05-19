'''
5. Longest Palindromic Substring
Medium

20017

1156

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
def longestPalindrome(s):
    
    tempTable = [[0 for i in range(len(s))] for j in range(len(s))]
    
    for i in range(len(s)):
        tempTable[i][i] = 1
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if j-i == 1:
                    tempTable[i][j] = 1
                else:
                    tempTable[i][j] = tempTable[i+1][j-1]
            else:
                tempTable[i][j] = 0
    
    maxLen = 0
    maxIndex = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if tempTable[i][j] > maxLen:
                maxLen = tempTable[i][j]
                maxIndex = i
    
    return s[maxIndex-maxLen+1:maxIndex+1]

    