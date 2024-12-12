a=int(input("enter basic salary "))
if(a<=10000 and a>1000):
    hra=(a*67)/100
    da = (a * 73) / 100
elif(a>=20000):
    hra = (a*73)/100
    da = (a * 89)/100
else:
    hra = (a * 69)/ 100
    da = (a * 76)/ 100
gross=hra+da+a
print("the gross salary is ",gross)