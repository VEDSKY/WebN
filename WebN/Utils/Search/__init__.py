from WebN.Sources import search


def on_search_query_changed(query):
    print(query)
    search_list = search(query)
    i = search_list
    for article in search_list:
        print(f"{article['author']}\n"
              f"{article['title']}\n"
              f"{article['description']}\n"
              f"{article['url']}\n"
              f"{article['urlToImage']}\n"
              f"{article['publishedAt']}\n"
              f"{article['content']}\n")
