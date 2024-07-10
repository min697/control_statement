# 점수구간에 해당하는 학점이 아래와 같이 정의되어 이다. 사용자로부터 스코어를 입력받아  학점으로 환산하여 출력
score = int(input("점수를 입력하시오."))
if 81 <= score <= 100 :
    print('A')
elif 61 <= score <= 80 :
    print('B')
elif 41 <= score <= 60 :
    print('C')
elif 21 <= score <= 40 :
    print('D')
elif 0 <= score <= 20 :
    print('F')