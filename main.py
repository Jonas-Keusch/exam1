i =1

while i <=50:
    if i%5==0:
        print("%d HiFive"%i)
    elif i%2==0:
        print("%d HiTwo"%i)
    elif (i%3==0) or (i%7==0):
        print("%d HiThreeOrSeven"%i)
    i+=1