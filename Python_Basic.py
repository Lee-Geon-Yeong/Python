#파이썬 기초 문법
'''
    # 이스케이프 시퀀스
        - 프로그램의 소스 코드 내에서 사용할 수 있도록
          백슬래시(\)기호와 조합해서 사용하는 사전에 정의해둔 문자 조합으로,
          문자열의 출력 결과를 제어하기 위해 사용함
        - \\ : 백슬래시(\)
        - \' : 작은따옴표(')
        - \" : 큰따옴표(")
        - \n : 줄바꿈
        - \t : 수평 탭

     # 문자열 포맷팅
        - %-포맷팅, str.format()함수를 이용한 문자열 포맷팅 제 
        >>> "키 : %s cm" %180.5
        '키 : 180.5 cm'
        >>> "%10s " & "우측정렬"
        '______우측정렬'
        >>> "%-10s " % "좌측정렬"
        '좌측정렬______'
        >>>"이름 : {0}, 나이 : {1} 세".format("홍길동", 20)
        '이름 : 홍길동, 나이 : 20세'
        >>>"이름 : {name}, 나이 : {age}세".format(name="홍길동", age=20)
        '이름 : 홍길동, 나이 : 20세'
        >>>"{0:<10}".format("좌측정렬")
        '좌측정렬______'
        >>>"{0:>10}".format("우측정렬")
        '______우측정렬'
        >>>"{0:^10}".format("중앙정렬")
        '___좌측정렬___'
        >>>"{0:*^10}".format("중앙정렬")
        '***좌측정렬***'
        >>>"{0:0.2f}".format(3.141592)
        '3.14'
'''
#

#파이썬 변수

'''
    # 변수의 자료형을 확인하는 방법
        type(num), type(str), type(lst)

    # 변수는 객체로 이루어짐
         >>>var1=10
         >>>var2=10
         >>>var1 is var2  -> 10을 var1과 var2가 참조
         
    # (Tuple)형
     - ()안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
     - 0부터 시작하는 인덱스를 이용해 접근할 수 있음. 한번 저장된 항목은 변경할 수 없음
     >>> student = ("홍길동", 20) -> 저장된 항목 변경 불가능 !!!(에러)
     >>> student[0]
     '홍길동'
     >>> student[1]
     20
     
    # [List]형
     - []안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
     - 0부터 시작하는 인덱스를 이용해 접근할 수 있음. 한번 저장된 항목이라도 변경할 수 있음
     >>> student = ["홍길동", 20] -> 저장된 항목 변경 가능 !!!!

    # {Set}형
     - {}안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
     - 순서의 개념이 존재하지 않아 인덱스를 사용할 수 없음
     - 데이터 항목의 중복을 허용하지 않음
     - 집합의 개념을 가지고 있는 자료구조로 합집합 연산자 제공
     >>>student = {"홍길동", "이순신", "강감찬", "홍길동"}
     >>>student
     {'홍길동','이순신','강감찬'}
     >>>student |= {"을지문덕", 이순신"}
     >>>student
     {'홍길동','이순신','강감찬', '을지문덕'}

    # {키:값} 딕셔너리형
        - {}안에 키:값 형식의 항목을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
        - 키를 이용해 값을 읽어 올 수 있음
        >>>dogs = {1: "골든리트리버", 2: "진돗개", 3: "보더콜리"}
        >>>dogs[1]
        '골든리트리버'
        dogs["4"]="알래스카말라뮤트" ->새로운 항목 추가 할 때 문자열로 해줘야함
        
    # None 객채를 이용해 널(null) 객체 상태를 표현함
        >>>obj=None

    # 변수의 제거
        >>>x=10, y=20
        >>>del(x)
        >>>del(y)
         
'''
#

# 연산자
'''
    # 산술연산자
        // : 좌변의 값을 우변의 값으로 나눈 몫 -> a=3//2 # a=1
        ** : 좌변의 값을 우변의 값으로 제곱 -> a=3**2 # a=9

        >>>a,b=3,2
        >>>print("{0}+{1}={2}".format(a,b,a+b))
        3+2=5

        >>>a, b, c = "2", "3", 4
        >>>print(a + b)
        23
        >>>print(int(a)+int(b))
        5
        
    # 비트연산자
        & : 양변의 비트 값 모두 1일 경우에만 1 반환
        | : 양변의 값 모두 0일 때만 0 반환
        ^ : 양변의 값이 다를 경우 1, 같을 경우 0 반환
        ~ : 비트 값이 1일 경우 0, 0일 경우 1 반환
        << : 좌변의 값을 우변의 값 만큼 비트 왼쪽으로 이동
        >> : 좌변의 값을 우변의 값 만큼 비트를 오른쪽으로 이동
        
    -> 괄호가 최우선, 산술연산이 비트연산보다 우선, 관계연산이 논리연산보다 우선    

'''
#
