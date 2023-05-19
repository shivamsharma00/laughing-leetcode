'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

# ? My method

def reverseWords(s):
    count = 0
    s1 = ""
    s2 = ""
    s+= " "
    for i in range(len(s)):
        
        if s[i] == " ":
            for j in range(len(s2)-1, -1, -1):
                s1 = s1 + s2[j]
            
            if i == len(s)-1:
                print("here")
                continue
            else:
                s1 = s1 + " "
            s2 = ""    
            # i+=1
        else:
            s2 += s[i]
      
    return s1

# ! alternate method

def reverseWords1(s):
    s = s.split()
    word = ""
    for i in s:
        i = i[::-1]
        word += i + " "
    # s = s[::-1]
    return word


if __name__  == '__main__':
    print(len("Let's take LeetCode contest"))
    print(len(reverseWords("Let's take LeetCode contest")))
    print(reverseWords1("Let's take LeetCode contest"))


