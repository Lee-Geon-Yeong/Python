#[SW expert academy] 4828. 1일차 - min max
# map()-> map(func, x)의 형태로 사용, 리스트 같은 x 각 요소에 func를 적용시켜 주는 함수
# 즉 a=list(map(int, input().split())) -> split는 공백문자를 기준으로 문자 잘라서 입력, split('-')이면 -기준으로 잘라서 입력
# a, *b = map(int, input().split()) -> a만큼 b배열에 변수 입력
T = int(input())
result=[]
MIN=''
MAX=''

for i in range(T):
    N = int(input())
    digit=list(map(int,input().split()))
    if(len(digit)!=N):
        digit = list(map(int, input().split()))
    MIN=min(digit)
    MAX=max(digit)
    temp=MAX-MIN
    result.append(temp)

for k in range(len(result)):
    print('#%d %d' % (k+1, result[k]))


