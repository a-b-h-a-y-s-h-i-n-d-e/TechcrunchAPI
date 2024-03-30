from fastapi import FastAPI
from lxml import html
import requests
import uvicorn

app = FastAPI()
TECHCRUNCH_URL = "https://techcrunch.com/"

@app.get('/')
async def getLatestArticles():
    response = requests.get(TECHCRUNCH_URL)
    
    if response.status_code == 200:    

        page = html.fromstring(response.content)
        divContent = [element.text for element in page.xpath("//a[@class='post-block__title__link']")]

        newsDictionary = {i + 1: text for i, text in enumerate(divContent)}
        # removing \t\n
        newsDictionary = {key: value.strip() for key, value in newsDictionary.items()}
        # removing empty key-value like this ""
        newsDictionary = {key: value for key, value in newsDictionary.items() if value.strip() != ""}
     
        return newsDictionary
    else:
        return {"error" : "Failed to fetch data from Techcrunch!"}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)

