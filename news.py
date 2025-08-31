import requests
# key = "356ec78cde824cc699fd46efd3b011ca"
API = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=356ec78cde824cc699fd46efd3b011ca"


response = requests.get(API)
final_response = response.json()

source = final_response["articles"][0]["source"]["name"]
author = final_response["articles"][0]["author"]
main = final_response["articles"][0]["description"]
final_ans = f"From {source}. writen by {author}. so the news is {main}"