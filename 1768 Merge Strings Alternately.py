#  Problem URL : https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)

        result = ""

        for i in range(max(w1_len, w2_len)):
            if i < w1_len:
                result+=(word1[i])
            if i < w2_len:
                result+=(word2[i])
        
        # if w1_len < w2_len:
        #     result+=(word2[w1_len:])
        # if w1_len > w2_len:
        #     result+=(word1[w2_len:])
        
        return result