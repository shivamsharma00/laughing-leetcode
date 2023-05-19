'''
443. String Compression
Medium

2228

4381

Add to List

Share
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''

# ? My method

def compress(s):
    result = []
    s2 = set(s)
    for i in s2:
        result.append(i)
        count = s.count(i)
        if count > 1:
            result.append(str(count))
    return result


# ! Alternate method

def compres1(char):

    # Two pointer method - slow and fast pointer

    s = f = 0
    c = len(char)

    while f < c:

        char[s] = char[f]
        count = 1

        while (f+1 < c) and (char[f] == char[f+1]):
            count += 1
            f += 1

        if count > 1:
            for i in str(count):
                char[s+1] = i
                s += 1
           
        s += 1
        f += 1

    return s    


if __name__ == '__main__':
    print(compres1(["a","a","b","b","c","c","c"]))