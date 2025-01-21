class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"