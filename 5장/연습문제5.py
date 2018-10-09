import random
x1=random.randint(1,100)
x2=random.randint(1,100)
num=int(input(str(x1) + "-" + str(x2) + "="))
if(num==x1-x2):
    print("맞습니다.")
else:
    print("틀렸습니다.")
