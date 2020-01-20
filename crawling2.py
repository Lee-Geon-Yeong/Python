from urllib.request import urlopen


try : 
    htmlObj=urlopen("http://pytho5nscraping.com/pages/page1.html")

except :
    print("dhghfl")
    
else :
    print(htmlObj.read())
