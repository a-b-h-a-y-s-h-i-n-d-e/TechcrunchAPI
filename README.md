# FastAPI TechCrunch Scraper

This is a FastAPI application that scrapes the latest articles from TechCrunch.

## Features

- Fetches the latest articles from TechCrunch website.
- Returns the article titles in a dictionary format.

## Code to use this API

```
import requests

response = requests.get("https://techcrunch-api-abhays-projects-bdb1b6d4.vercel.app/")
print(response.json())

```
