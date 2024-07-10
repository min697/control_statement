# 홀/짝수 판독기 프로그램
# 사용자 수 입력
num = int(input("임의의 수를 입력하세요"))
# 홀수인지 짝수인지 (%)
data = num % 2
if data == 0:
    print('짝수')
else :
    print('홀수')