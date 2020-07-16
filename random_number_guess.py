import random

def rand(start, end):
    number = int(random.random() * (end - start + 1)) + start
    return number

def main():
    start = 1
    end = 10
    cnt=1
    number = rand(start, end)
    for i in range(10):
        anser=int(input("%d번째 추측값 : "%cnt))
        if number == anser :
            print("정답입니다")
            break
        elif number>anser :
            print("%d보다는 큽니다"%anser)
            cnt+=1
        else :
            print("%d보다는 작습니다"%anser)
            cnt+=1
        if cnt>5 :
            print("실패했습니다")
            break
main()
