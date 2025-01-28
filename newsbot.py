import feedparser

def fetch_rss_bbc():
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_url)
    
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link})
    return articles

    

    


def fetch_nytimes_rss():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})

    return articles


def fetch_nytimes_africa():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_americas():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_americas():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_asiapac():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_europe():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_middleast():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_all_nytimes_news():
    regions = {
        "World": fetch_nytimes_rss(),
        "Africa": fetch_nytimes_africa(),
        "Americas": fetch_nytimes_americas(),
        "Asia Pacific": fetch_nytimes_asiapac(),
        "Europe": fetch_nytimes_europe(),
        "Middle East": fetch_nytimes_middleast(),
    }

    all_articles = []
    for region, articles in regions.items():
        for article in articles:
            all_articles.append({
                "region": region,
                "title": article["title"],
                "link": article["link"],
                "description": article["description"]
            })

    return all_articles


# all_news = fetch_all_nytimes_news()
# for article in all_news:
#     print(f"[{article['region']}] {article['title']}\nLink: {article['link']}\nDescription: {article['description']}\n")
