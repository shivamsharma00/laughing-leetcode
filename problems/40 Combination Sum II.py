'''
40. Combination Sum II
Solved
Medium
Topics
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        stack = []

        def rec(ind, target):

            if target == 0:
                ans.append(stack[:])
                return
            
            for i in range(ind, len(candidates)):

                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                
                if candidates[i] <= target:
                    stack.append(candidates[i])
                    rec(i+1, target-candidates[i])
                    stack.pop()
                else:
                    break
        rec(0, target)
        return ans