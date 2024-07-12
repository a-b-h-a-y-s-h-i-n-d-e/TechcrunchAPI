from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lxml import html
import requests
import uvicorn

app = FastAPI()
TECHCRUNCH_URL = "https://techcrunch.com/"

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:80",
    "http://localhost:443",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def getLatestArticles():
    response = requests.get(TECHCRUNCH_URL)
    
    if response.status_code == 200:    

        page = html.fromstring(response.content)
        newsDictionary = {}
        for element in page.xpath("//h2[@class='has-link-color wp-block-post-title has-h-5-font-size wp-elements-565fa7bab0152bfdca0217543865c205']/a"):
            title = element.text.strip().replace('\n', '').replace('\t', '')
            print("title ->", title)
            url = element.get('href')
            if title:
                newsDictionary[title] = url


     
        return newsDictionary
    else:
        return {"error" : "Failed to fetch data from Techcrunch!"}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)