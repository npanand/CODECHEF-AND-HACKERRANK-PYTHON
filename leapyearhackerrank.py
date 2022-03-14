def is_leap(year):
    a=year
    c=a%4
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                leap=True
            else:
                leap= False
        else:
            leap=True
    else:
        leap= False
    return leap 