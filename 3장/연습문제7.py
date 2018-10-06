# 현재 시간
import time
#1970년 1월 1일부터의 시간(초로 반환)
fseconds=time.time()
print("현재 시간(영국 그리니치 시각) : ", (int)(fseconds//60%24), "시 ", (int)(fseconds%60), "분")
