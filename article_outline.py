class ArticleOutline:
    def __init__(self, title, link, date, org):
        super().__init__()

        self.title = title
        self.link = link
        self.date = date
        self.org = org

    def printArticleOutline(self):
        print({"title": self.title, "link": self.link, "date": self.date, "org": self.org})

    def toJSON(self):
        return {"title": self.title, "link": self.link, "date": self.date, "org": self.org}