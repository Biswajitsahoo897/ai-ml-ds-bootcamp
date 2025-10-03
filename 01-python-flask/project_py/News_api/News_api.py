import dotenv ,os,requests
# load dotenv
dotenv.load_dotenv()
# API key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# query="Artificial Intelligence"
input_query=input("what type of news are you interested in ? \n")
query=input_query.replace(" ","-")

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-10-02&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

r=requests.get(url)
data=r.json()
# print(data)
articles=data["articles"]
# print(f"This is the url : {url}")

for i, article in enumerate(articles, start=1):
    print("********************")
    print(f"{i}. {article['title']}")
    print("********************\n")
    print("Description:",article["description"],"\n")