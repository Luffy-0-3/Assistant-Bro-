import requests
from datetime import date

def headlines(query):
    api = "YOUR_NEWSAPI_KEY"  # Use your own NewsAPI key here
    today_date = date.today()

    url = f"https://newsapi.org/v2/everything?q={query}&from={today_date}&sortBy=publishedAt&apiKey={api}"
    
    r = requests.get(url)
    data = r.json()
    articles = data["articles"]
    
    for index, article in enumerate(articles):
        print(index, article["title"])
        print(article["url"])
        print("\n -------------------------------------------------- \n")
