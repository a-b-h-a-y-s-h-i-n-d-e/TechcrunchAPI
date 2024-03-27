from fastapi import FastAPI
from lxml import html
import requests

app = FastAPI()
TECHCRUNCH_URL = "https://techcrunch.com/"


@app.get('/')
def getLatestArticles():
    response = requests.get(TECHCRUNCH_URL)
    
    if response.status_code == 200:    

        
        page = html.fromstring(response.content)
        divContent = [element.text for element in page.xpath("//a[@class='post-block__title__link']")]
        newsDictionary = {i + 1: text for i, text in enumerate(divContent)}
        newsDictionary = {key: value.strip() for key, value in newsDictionary.items()}
        newsDictionary = {key: value for key, value in newsDictionary.items() if value.strip() != ""}
     
        return newsDictionary
    else:
        return {"error" : "Failed to fetch data from Techcrunch"}


    
    