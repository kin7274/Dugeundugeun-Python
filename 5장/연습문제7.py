import random

num=int(input("복권번호를 입력하세요(0에서 99사이) : "))
x=random.randint(0,99)
a1=num//10
a2=num%10
b1=x//10
b2=x%10
print("당첨번호는 ", x, " 입니다.")
if(x==num):
    print("축 상금100")
elif(a1==b1 or a1==b2 or a2==b1 or a2==b2):
    print("상금은 50만원")
else:
    print("상금은 없습니다.")
