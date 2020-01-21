# 1~9 사이의 정수 a를 입력받아 a+aa+aaa+aaaa의 값을 계산하는 프로그램을 작성하시오.

#입력 9
#출력 11106

a = int(input())

print(int("{a}".format(a=a)) + int("{a}{a}".format(a=a)) + int("{a}{a}{a}".format(a=a)) + int("{a}{a}{a}{a}".format(a=a)))
