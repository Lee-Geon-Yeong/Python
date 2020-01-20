from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot

url="http://pythonscraping.com/pages/warandpeace.html"
try :
    htmlObj=urlopen(url)
except :
    print("요청 제대로 되지 않았습니다")
else :
    bsObj=BeautifulSoup(htmlObj, "lxml")

    findObj=bsObj.find("span", {"class":"red"})
    textObj=findObj.getText()

    textObj=textObj.replace('\n', '')
    textObj=textObj.replace('-', '')
    textObj=textObj.replace(',', '')
    textObj=textObj.replace('.', '')
    textObj=textObj.replace('!', '')
    
    splObj=textObj.split(' ')
    word_freq={}
    for word in splObj :
        word_freq.setdefault(word, 0)
        word_freq[word]+=1
    
    x= []
    y= []
    for word in word_freq :
        if word_freq[word] >= 2 :
            x.append(word)
            y.append(word_freq[word])

    pyplot.bar(x, y)
    pyplot.xlabel("word")
    pyplot.ylabel("frequency")
    pyplot.title("words' frequency")
    pyplot.show()

    with open("wordcount.csv", 'w') as myFile :
        myFile.write("words' frequency\n")
        for word in word_freq :
            myFile.write("{0}, {1}\n".format(word, word_freq[word]))
            
            



            


        
    
