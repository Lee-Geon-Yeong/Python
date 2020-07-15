import random
ROCK=0
SCISSORS=1
PAPER=2
DROW=0
WIN=0
LOSE=0
for num in range(3):
    com=random.randint(0,2)
    me=int(input("가위바위보\n"))
    if com==me:
        print("%d번째 : 비김" %(num+1))
        DROW+=1
    elif com==ROCK:
        if me==SCISSORS:
            print("%d번째 : 컴퓨터가 이김" %(num+1))
            LOSE+=1
        else:
            print("%d번째 : 내가 이김" %(num+1))
            WIN+=1
    elif com==SCISSORS:
        if me==PAPER:
            print("%d번째 : 컴퓨터가 이김" %(num+1))
            LOSE+=1
        else:
            print("%d번째 : 내가 이김" %(num+1))
            WIN+=1
    elif com==PAPER:
        if me==ROCK:
            print("%d번째 : 컴퓨터가 이김" %(num+1))
            LOSE+=1
        else:
            print("%d번째 : 내가 이김" %(num+1))
            WIN+=1
print("승 : %d 패 : %d 무 : %d" %(WIN, LOSE, DROW))
# 여러 줄 주석 하고싶을 때는 범위 드래그 후 ctrl+/