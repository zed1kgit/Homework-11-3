from abc import ABC, abstractmethod
from book_product import BookList


class BookCreator(ABC):
    @abstractmethod
    def create_book(self, tittle, year, author):
        pass

    @abstractmethod
    def remove_book(self, tittle):
        pass

    @abstractmethod
    def change_book(self, tittle, name_of_data, data):
        pass

    @abstractmethod
    def search_book(self, tittle):
        pass

    @abstractmethod
    def save_to_json(self):
        pass

    @abstractmethod
    def load_from_json(self):
        pass

    @abstractmethod
    def search_book_index(self, tittle):
        pass


class CreateBookList(BookCreator):
    def create_book(self, tittle, year, author):
        return BookList().create_book(tittle, year, author)

    def remove_book(self, tittle):
        return BookList().remove_book(tittle)

    def change_book(self, tittle, name_of_data, data):
        return BookList().change_book(tittle, name_of_data, data)

    def search_book(self, tittle):
        return BookList().search_book(tittle)

    def save_to_json(self):
        return BookList().save_to_json()

    def load_from_json(self):
        return BookList().load_from_json()

    def search_book_index(self, tittle):
        return BookList().search_book_index(tittle)
