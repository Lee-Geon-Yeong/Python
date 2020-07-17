T=int(input())

for i in range(1, T+1):
    N=int(input())
    arr=list(map(int, input()))

    max_num=-1
    max_cnt=0
    for j in range(10):
        if arr.count(j)>=max_cnt:
            max_cnt=arr.count(j)
            max_num=j

    print("#{} {} {}".format(i, max_num, max_cnt))