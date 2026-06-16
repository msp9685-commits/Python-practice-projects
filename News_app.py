'''Create a News App in Python by integrating with news APIs like NewsAPI.
This app will fetch the latest headlines, display articles, and allow users to filter news based on categories or keywords.
It helps you practice working with APIs, handling JSON data, and building user interfaces.'''
import os
from newsapi import NewsApiClient
key = input("enter your key")

api = NewsApiClient(api_key=key)
choice = input("search by category or keyword")
if choice == "category":
    category = input("enter the category for which you want news ")
    data = api.get_top_headlines(category=category)
elif choice == "keyword":
    keyword = input("enter the key word ")
    data = api.get_everything(q=keyword)
else: 
    print("invalid choice")

if not data["articles"]:
    print("No news found.")
else:
    for article in data["articles"]:
        print(article["title"])
        print(article["description"])
        print("Source:", article["source"]["name"])
        print("url:", article["url"])
        print("-" * 40)

