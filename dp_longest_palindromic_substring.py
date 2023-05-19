'''
Given a string s, return the longest 
palindromic
 
substring
 in s.
'''
# DynamicProgramming

def longest_palindrome(str1):
    # initializing matrix to store all palindrome length  
    dp_mat = [[False for i in range(len(str1))] for i in range(len(str1)) ]
    n = len(str1)

    for i in range(n):
        for j in range(n):
            if i==j:
                dp_mat[i][j] = True

    palin_str = str1[0]

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):

            if str1[i] == str1[j]:

                if (j-i) == 1 or dp_mat[i+1][j-1]:
                    # l1 = len(str1[i][j+1])
                    dp_mat[i][j] = True

                    if len(palin_str) < len(str1[i:j+1]):
                        palin_str = str1[i:j+1]
     
            # if dp_mat[i+1][j-1] == 0:
            #     dp_mat[i][j] = 0
            # else:
            #     print(f"str[1]-{str1[i]}, str1[j]-{str1[j]}")
            #     if str1[i] == str1[j]:
            #         new_len = dp_mat[i+1][j-1] + 2
            #         dp_mat[i][j] = new_len
            #         if new_len < max_len:
            #             max_len = new_len
            #             max_index = i
            # print(dp_mat)
            
    print(dp_mat)

    # if max_index == 0:
    #     final_str = str1[max_index:max_len]
    # else:
    #     final_str = str1[max_index:max_len+max_index]\
    if len(str1) ==1 :
        palin_str = str1

    return palin_str

if __name__ == '__main__':
    # s1 = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
    s1 = 'ac'
    print(longest_palindrome(str1=s1))