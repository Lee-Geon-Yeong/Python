import urllib.request 
import json 

client_id = "rOc74uqftZkAWrS9HBLS"
client_secret = "Q7Q17I1bOs"
serch_text = urllib.parse.quote("빅데이터")
page_start = 1
display = 5

url = "https://openapi.naver.com/v1/search/news?query=%s&start=%s&display=%s"%(serch_text, page_start, display)

reqObj=urllib.request.Request(url)
print(reqObj)

reqObj.add_header("X-Naver-Client-Id", client_id)
reqObj.add_header("X-Naver-Client-Secret", client_secret)

htmlObj = urllib.request.urlopen(reqObj)
print(htmlObj)

htmlObj_body = htmlObj.read()
htmlObj_body= htmlObj_body.decode('utf-8')


with open('result.json', 'w+') as json_file:
    json.dump(htmlObj_body, json_file)
