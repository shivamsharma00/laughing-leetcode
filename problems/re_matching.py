'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''

def isMatch(s, p):

    # recursive 
    print(f"s-{s}, p-{p}")

    if not p:
        return not s
    
    first_word = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or (first_word and isMatch(s[1:], p))
    else:
        return (first_word and isMatch(s[1:], p[1:]))
   


if __name__ == '__main__':
    s1 = 'aa'
    p1 = 'a'
    s2 = 'aa'
    p2 = "a*"
    s3 = "ab"
    p3 = ".*"
    s4 = "aab"
    p4 = "c*a*b"
    s5 = "aaa"
    p5 = "ab*ac*a"

    print(isMatch(s1, p1)) 