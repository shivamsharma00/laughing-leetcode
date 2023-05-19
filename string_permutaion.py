'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

def checkInclusion(s1, s2):
    l1 = len(s1)
    sd1 = {}
    sd2 = {}
    
    for i in s1:
        sd1[i] = sd1.get(i, 0) + 1
    l = 0
    for i in range(len(s2)+1):

        if i >= l1:
            if sd1 == sd2:
                return True

            sd2[s2[l]] -= 1
            if sd2[s2[l]] == 0:
                sd2.pop(s2[l])
            l += 1

        if i < len(s2):
            if s2[i] not in sd2:
                sd2[s2[i]] = 1
            else:
                sd2[s2[i]] += 1
        
    return False



    
    

if __name__ == '__main__':

    print(checkInclusion("ab", "eidbaooo"))