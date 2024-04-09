"""
This code converts integers to roman numbers
"""

rn = ""
num = 4239
flag = True

while flag:

    if  num<5:
        if num==4:
            rn+="IV"
            flag = False
        else:
            rn+=("I"*num)
            flag = False
    
    elif num == 5:
        rn+="V"
        flag = False
    
    elif num<10:
        if num == 9:
            rn+="IX"
            flag = False
        else:
            rn+="V"
            num = num - 5
    
    elif num == 10:
        rn+="X"
        flag = False
    
    elif num<50:
        if num >= 40:
            rn+="XL"
            num = num%40
        else:
            rn+=("X"*(num//10))
            num = num - (10*(num//10))
    
    elif num == 50:
        rn += "L"
        flag = False
    
    elif num<100:
        if num >= 90:
            rn+="XC"
            num = num%90
        else:
            rn+="L"
            num = num - 50
    
    elif num == 100:
        rn+="C"
        flag = False
    
    elif num<500:
        if num>=400:
            rn+="CD"
            num = num%400
        else:
            rn+=("C"*(num//100))
            num = num - (100 * (num//100))

    elif num<1000:
        if num>=900:
            rn+="CM"
            num = num%900
        else:
            rn+="D"
            num = num - 500

    elif num == 1000:
        rn+="M"
    else:
        rn+= "M"*(num//1000)
        num = num - (1000 * (num//1000))

print(rn)