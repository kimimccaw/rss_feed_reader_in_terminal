import feedparser
class feed_parsing:
    def feed_parser(self,url):
        self.d = feedparser.parse(url)
    
    def get_feed_title(self):
        return self.d.feed.title

    def get_feed_description(self):
        return self.d.feed.description

    def get_feed_link(self):
        return self.d.feed.link

if __name__ == "__main__":
    url = input("Insert your link: ")
    link = feed_parsing()
    link.feed_parser(url)


    print("RSS feed Title: ",link.get_feed_title())
    print("Feed Description: " ,link.get_feed_description())
    print("Original Link: " ,link.get_feed_link())