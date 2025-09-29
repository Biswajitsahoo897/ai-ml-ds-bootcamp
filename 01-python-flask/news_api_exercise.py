# import requests
# import json

# # Define your API key and the endpoint URL
# query = input("what type of news are you interested in now :-")  # Replace this with your actual API key
# url = f"https://newsapi.org/v2/everything?q={query}&from=2024-09-05&sortBy=publishedAt&apiKey=dfa299ec1f9b4c35a348d0e3a71075c4"

# # Make the request to the News API
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the response JSON
#     news_data = response.json()

#     # Display the articles
#     print("Top Headlines:")
#     for i, article in enumerate(news_data["articles"], start=1):
#         print(f"{i}. {article['title']} - {article['source']['name']}")
# else:
#     print(f"Failed to retrieve news articles. Status code: {response.status_code}")



# import requests
# import json

# query = input("What type of news are you interested in? ")
# # Specify the language parameter to get results in English
# url = f"https://newsapi.org/v2/everything?q={query}&from=2024-09-05&sortBy=publishedAt&language=en&apiKey=dfa299ec1f9b4c35a348d0e3a71075c4"
# r = requests.get(url)
# news = json.loads(r.text)

# for article in news["articles"]:
#     print(article["title"])
#     print(article["description"])
#     print("--------------------------------------")


import requests,json
url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'language=en'
        'apiKey=dfa299ec1f9b4c35a348d0e3a71075c4')
response = requests.get(url)
news=json.loads(response.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------")
# print (response.json())