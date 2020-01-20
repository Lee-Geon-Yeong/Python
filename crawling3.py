from urllib.request import urlopen
from bs4 import BeautifulSoup

url="http://pythonscraping.com/pages/warandpeace.html"


try :
    htmlObj=urlopen(url)

except :
    print("error")

else :
    bsObj=BeautifulSoup(htmlObj, "lxml")
#    nameList=bsObj.findAll("span", {"class" : "green"})
#    for name in nameList :
#        print_name=name.get_text()
#        print_name=print_name.replace('\n', ' ')
#        print(print_name)

    princeText=bsObj.findAll(text="the Empress")

    n=len(princeText)
    print("the Empress " +str(n) + "회 나타남")
    print("--------------")

    for i in princeText :
        print(i)

    print("\n \n")
    


    
