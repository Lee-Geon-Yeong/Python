users = {
    "go": "g1234",
    "hong": "h1234",
    "kim": "k1234",
    "na": "n1234",
    "al": "a1234"
}


def get_user_info():
    user_id = input("사용자 ID :")
    password = input("비밀번호 :")

    return user_id, password


def check_login(user_id, password):
    if user_id not in users:
        print(f"{user_id}는 존재하지 않는 ID 입니다.")
        return False
    elif users[user_id] == password:
        return True
    else:
        print(f"비밀번호가 틀렸습니다.")
        return False

def print_result(result, user_id):
    if result:
        print(f"로그인에 성공했습니다.  반갑습니다. {user_id}님")
    else:
        print("로그인에 실패했습니다. \n다음 기회에...")


def main():
    result = False      # 로그인 결과 상태 저장, 디폴트 False

    for i in range(3):  # 최대 3회 시도
        user_id, password = get_user_info()     # User ID, Password  입력
        result = check_login(user_id, password) # 로그인 검사
        if result:      # 로그인 성공시 탈출
            break

    print_result(result, user_id)   # 결과 출력


main()
