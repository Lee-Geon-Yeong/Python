# 파일 쓰기
# r : 읽기, 파일이 없는 경우 예외 발생
# w : 쓰기, 파일이 없으면 새로 생김
# a : 추가
# x : 쓰기용으로 여나 기존 파일이 있는 경우 실패
# t : text 모드로 열기
# b : binary 모드로 열기
f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라
!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close()

# 파일 읽기
# f.read() -> 파일 전체 내용
# f.read(n) -> n개의 내용
# f.readline() -> 한 줄
# f.readlines() -> 전체 라인 리스트
# - 각 라인의 끝에 개행 문자가 들어 있음
try:
 f = open("live.txt", "rt")
 text = f.read()
 print(text)
except FileNotFoundError:
 print("파일이 없습니다.")
finally:
 f.close()

