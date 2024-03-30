'''
326. Power of Three
Solved
Easy
Topics
Companies
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        METHOD 1:

        if n==1:
            return True
        while n>=3 and n%3==0:
            n = n//3

            if n==1:
                return True
        
        return False

        '''
        
        if n<=0:
            return False
        
        logV = log10(n)/log10(3)
        return logV==int(logV)