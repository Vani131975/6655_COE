project=int(input("give project score "))
internal=int(input("give internal score "))
external=int(input("give external score "))
if(project>=50 and internal>=50 and external>=50):
    pro_sc = (project * 70) / 100
    int_score = (internal * 10) / 100
    ext_score = (external * 20) / 100
    total = pro_sc + int_score + ext_score
    if(total>90):
       print("A grade")
    elif(total>80 and total<=90):
        print("B grade")
    else:
        print("C grade")
else:
    if(internal<50):
        print("student failed in internal ",internal," score")
    if (external < 50):
        print("student failed in external ", external, " score")
    if(project<50):
        print("student failed in project ", project, " score")