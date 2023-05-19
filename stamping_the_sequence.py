'''
ou are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

 
'''
def movesToStamp(stamp, target):
    
    s = ["-"] * len(target)
    no_of_try = 10 * len(target)
    stamp_index = []

    tries = [i for i in range(len(target) - len(stamp)+1)]
    flag = False

    def cM(stamp, target, s, stamp_index, tries):
        
        print(f"s-{s}, tries-{tries}")
        tr = tries
        if len(tr) > 0:
            for i in tr:
                for j in range(len(stamp)):
                    s[i+j] = stamp[j]

                stamp_index.append(i)
                tr.remove(i)
                c = cM(stamp, target, s, stamp_index, tr)
                if c == None:
                    pass
        else:
            return None
            
    def calMoves(stamp, target, s, stamp_index, tries):
        print("".join(s))
        # print(f"tries-{tries}")

        if str("".join(s)) == target:
            # print("ere")
            # flag = True
            # return flag, stamp_index
            return stamp_index
        else:
            # while len(tries) > 0:

            if len(tries) > 0:
                for i in tries:
                    
                    # print(f"i-{i}, {tries}, {stamp_index}")
                    for j in range(len(stamp)):
                        s[i+j] = stamp[j]
                
                    stamp_index.append(i)
                    tries.remove(i)
                    # print(f"s-{s}, stamp_index-{stamp_index}, tries-{tries}")
                    si = calMoves(stamp, target, s, stamp_index, tries)
                    print(f"i-{i}, s-{s}, stamp_index-{stamp_index}, tries-{tries}, si-{si}")
                    
                    if len(si):
                        return si
                    else:
                        print(f"Here, tries-{tries}")
                        # return calMoves(stamp, target, s, stamp_index, tries)
                        return []
                        # flag2, si1 = calMoves(stamp, target, s, stamp_index, tries)
            else:
                return []
        
        if len(stamp_index) >= no_of_try:
            stamp_index = []
            # flag = False
            return stamp_index

        
        # else:
        #     print("Here")
        #     return []
    cM(stamp, target, s, stamp_index, tries)
    # return calMoves(stamp, target, s, stamp_index, tries)
         

if __name__ == "__main__":
    
    stamp1 = "abc"
    target1 = "ababc"

    stamp2 = "abca"
    target2 = "aabcaca"

    print(movesToStamp(stamp1, target1))