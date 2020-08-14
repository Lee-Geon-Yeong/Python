* 장고 정보
 패키지->middleware(모듈을 모아놓은 것 __init__ 반드시 필요)
 {#템플릿 주석#}
 Ctrl+Alt+Shift+L ->코드정렬
 python으로 웹 페이지를 구축할 때 가장 인기있는 프레임워크는 django이다.
 장고-> MVT 코딩순서에 맞춰 프로젝트 개발
  1. 프로젝트 뼈대 만들기 : 프로젝트 및 앱 개발에 필요한 디렉토리와 파일 생성
  2. 모델 코딩하기 : 테이블 관련 사항을 개발(models.py, admin.py파일)
  3. URL conf 코딩하기 : URL 및 뷰 매핑 관계를 정의(Urls.py파일)
  4. 템플릿 코딩하기 : 화면 UI 개발(templates/디렉토리 하위의 *html 파일들)
  5. 뷰 코딩하기 : 애플리케이션 로직 개발(views.py 파일)



* 가상환경 만들기
 1. Heidisql 열기 -> 세션 관리자
 2. root 접속 -> CREATE DATABASE django_ex_db;
                 SHOW DATABASES;
 3. CREATE USER 'webuser'@'%' IDENTIFIED BY '1234'
    GRANT ALL PRIVILEGES ON django_ex_db.* to 'webuser'@'%'; -> 각각 개별 실행 -> 데이터베이스 생성
 4. 그 뒤로 PPT 보고 진행
 5. 프로젝트 뼈대 만들기 -> $python manage.py migrate -> 경로가 C:\원하는 디렉토리인지 , 데이터베이스 명, 사용자 ID, 비번 확인
 
* django
 $pip install django #장고 설치
 $python manage.py migrations #DB에 변경 필요한 사항 추출
 $python manage.py migrate #DB에 변경사항 반영
 $python manage.py runserver #서버 작동
 $python manage.py startapp boards #프로젝트 내부 boards라는 이름의 앱 생성
 # settings.py에서 파일 수정해서 프로젝트와 연결
 > Django\settings.py
INSTALLED_APPS=[
    'boards.apps.BoardsConfig',
    'django.contrib.admin', 
    ...
]

* 핸드폰 연결
 ALLOWED_HOSTS=['192.168.0.30', '127.0.0.1', 'localhost']
 (webapp)c:\workspace\04.django\webapp>ipconfig
            > python manage.py runserver 0.0.0.0.8000

* 가상환경 만들기
cd 설치하고자 하는 폴더 위치
>pip install virtual env
>virtualenv venv
>call venv/scripts/activate
>(venv)>pip list
가상환경 탈출 -> deactivate
(venv)pip freeze>requirements.txt -> 설치한 목록 다음 명령어를 통해 정확한 리스트로 저장
