str=int(input("정수를 입력하시오 : "))
print("자리수의 합 : ", str//1000 + str//100%10 + str//10%10 + str%10)
