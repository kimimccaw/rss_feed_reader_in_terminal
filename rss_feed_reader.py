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

def main(url):
    link = feed_parsing()
    link.feed_parser(url)

    print("\n\nRSS feed Title: ",link.get_feed_title())
    print("Feed Description: " ,link.get_feed_description())
    print("Original Link: " ,link.get_feed_link())


    

if __name__ == "__main__":
    url = str(input("Add url: "))

    while url != str(0) :
                
        main(url)
        print("\n\nadd 0 to stop \n\n")
        url = str(input("Add url: "))
        if url == str(0):
            print("Program exit")