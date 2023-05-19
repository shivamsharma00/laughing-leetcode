'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this c
'''

def convert(s1, num_of_rows):
    # finiding number of columns
    diag_len = (0 if num_of_rows<2 else (num_of_rows-2))
    number_of_repeat_ele = num_of_rows + diag_len
    str_len = len(s1)
    total_int = int(str_len/number_of_repeat_ele)

    mod_of_total_r = (str_len%number_of_repeat_ele)
    extra_rows = 0
    dia_wr = 0
    v_col_write = total_int

    if mod_of_total_r != 0:
        extra_rows = (1 if mod_of_total_r<num_of_rows else (1+(mod_of_total_r)-num_of_rows))
        v_col_write = total_int + 1 
        if diag_len:
            dia_wr = ((total_int*diag_len + (0 if mod_of_total_r<num_of_rows else ((mod_of_total_r)-num_of_rows)))/diag_len).__ceil__()
        
    num_of_col = total_int + (total_int*diag_len) + extra_rows
    
    dp_mat = [[False for i in range(num_of_col) ] for j in range(num_of_rows)]

    print(dia_wr)
    w = 0
    v_col_in = 0
    for i in range(v_col_write):
        
        for j in range(num_of_rows):
            if w<str_len:
                dp_mat[j][v_col_in] = s1[w]
                w+=1
        v_col_in += diag_len + 1 
        w += diag_len

    c = 1
    w = num_of_rows
    for i in range(v_col_write):
        r = num_of_rows - 2        
        for x in range(diag_len):
            if w < str_len:
                dp_mat[r][c] = s1[w]
                w += 1
            r -=1
            c +=1
        c += 1
        w += num_of_rows


    for i in range(len(dp_mat)):
        print(dp_mat[i])
    
    final_str = ""
    for i in range(len(dp_mat)):
        for j in dp_mat[i]:
            if j:
                final_str+=(j)
    
    print(final_str)
    # print(dp_mat[i] for i in range(len(dp_mat))) 

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    n = 3
    print(convert(s, n))


