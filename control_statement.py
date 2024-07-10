# print("hello world")
# a = 10
# b = 3
#
# if 3>4 :
#     print ("3은 1보다 큽니다.")
#     print ("연산을 종료합니다.")
# print("_"*15)
# print ("저는 들여쓰기를 하지 않은 라인입니다.")
# if a + b < 14 :
#     print ('yeah, it is true.')
#
#
# a = "박민상"
# b = "박꽁식"
#
# # 같지 않냐? 다르지 않냐? 에대한 참 거짓 (!=)
# if a != b :
#     print("두 사람의 이름은 같습니다.")
#
#
# content = "감자"
# if content == "고구마" :
#     print ("그것은 고구마입니다.")
#
# if a==b :
#     print("두 사람의 이름은 같습니다."

num_1 = 10
num_2 = 3

if num_1 < num_2 :
    print('num_1은 num_2 보다 크기가 작습니다.')

elif num_1 == num_2 :
    print("num_1은 num_2랑 크기가 같습니다.")

elif num_1 > num_2 :
    print("num_1은 num_2보다 크기가 큽니다.")


# 조건식 두개를 써야 되는경우 and, or 연산자
apple = '사과'
banana = '감자'

if apple == '사과' or banana == '바나나' :
    print("문자열이 모두 정확합니다.")

# 내가 찾고자 하는 대상, 요소 찾는법
var = [1,2,3]
if 3 in var :
    print("숫자 3이 var 변수에 있습니다.")