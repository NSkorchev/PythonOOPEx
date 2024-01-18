from abc import abstractmethod, ABC


class Book:
    def __init__(self, content: str, title: str, author: str):
        self.content = content
        self.title = title
        self.author = author


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)
