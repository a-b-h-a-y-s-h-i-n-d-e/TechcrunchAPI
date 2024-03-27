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
        title = page.xpath("//div[@class='feature-island']/div/h2/a/text()")
        return {"text" : title}
    else:
        return {"error" : "Failed to fetch data from Techcrunch"}


    
    