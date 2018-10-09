import random

options=["왼쪽", "중앙", "오른쪽"]
com_choice=random.choice(options)
user_choice=input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽)")
if com_choice ==user_choice:
    print("수비 성공")
else:
    print("패널티킥 성공")
