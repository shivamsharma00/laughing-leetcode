def myAtoi(s):
    n = 0
    num = 0
    n_flag = False
    
    while (n<len(s)) and (s[n] == " " or s[n] == "+" or s[n]=="-" or s[n].isnumeric()):
        print(s[n])
        if s[n] == '-':
            n_flag = True
        elif s[n].isnumeric():
            num = ((num*10)+int(s[n]))
        n+=1
    
    num = -abs(num) if n_flag else abs(num)

    if num < -abs(2**31):
        num = -abs(2**31)
    elif num > abs(2**31 -1):
        num = abs(2**31 - 1)
    return num

    # for i in s:
    #     print(i)
    #     if i.isnumeric():
    #         n = ((n*10) + int(i))
    #     elif i == '-':
    #         n_flag=True
    
    # n = -abs(n) if n_flag else abs(n)
    # print(n)

if __name__ == "__main__":
    s = str("+-12")
    print(myAtoi(s))