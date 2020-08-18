from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot
from matplotlib import font_manager, rc
import matplotlib

url = "http://class.gnu.ac.kr/~elsa1122/bd/ex7.html"
try:
    htmlObj = urlopen(url)
except:
    print("요청 제대로 되지 않았습니다")
else:
    bsObj = BeautifulSoup(htmlObj, "lxml")

yearObj=bsObj.findAll("td", {"class":"td-year"})

year_cnt=[0,0,0,0,0,0,0]

for year in yearObj:
    if year.get_text()=="1":
        year_cnt[0]+=1
    elif year.get_text()=="2":
        year_cnt[1]+=1
    elif year.get_text()=="3":
        year_cnt[2]+=1
    elif year.get_text()=="4":
        year_cnt[3]+=1
    elif year.get_text()=="대학원생":
        year_cnt[4]+=1
    elif year.get_text()=="일반인":
        year_cnt[5]+=1
    else:
        year_cnt[6]+=1

print("1학년 : %d 명" %year_cnt[0])
print("2학년 : %d 명" %year_cnt[1])
print("3학년 : %d 명" %year_cnt[2])
print("4학년 : %d 명" %year_cnt[3])
print("대학원생 : %d 명" %year_cnt[4])
print("일반인 : %d 명" %year_cnt[5])
print("기타 : %d 명" %year_cnt[6])

#font_location="C:\\Project\\static\\fonts\\HoonWhitecatR.ttf"
#font_name=font_manager.FontProperties(fname=font_location).get_name()
#matplotlib.rc('font', family=font_name)

xList=["first-year", "second-year", "third-year", "fouth-year", "graduate student", "non-student", "etc"]

pyplot.bar(xList, year_cnt)
pyplot.xlabel("What grade are you in?")
pyplot.ylabel("How many people?")
pyplot.title("How many students per grade?")
pyplot.show()
