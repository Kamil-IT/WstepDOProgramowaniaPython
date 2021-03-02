class DiaryCard:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_date(self):
        return self.date
