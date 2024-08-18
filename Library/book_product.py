from abc import ABC, abstractmethod
import json


class BookProduct(ABC):
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


class BookList(BookProduct):
    book_list = []

    def create_book(self, tittle, year, author):
        created_book = {
            "tittle": tittle,
            "year": year,
            "author": author
        }
        BookList.book_list.append(created_book)
        return created_book

    @staticmethod
    def search_book_index(tittle):
        for i in range(len(BookList.book_list)):
            if BookList.book_list[i]["tittle"] == tittle:
                return i
        else:
            return None

    def remove_book(self, tittle):
        index = self.search_book_index(tittle)
        if index is not None:
            return f"Удаленная книга:\n{BookList.book_list.pop(index)}"
        else:
            return "Удаляемая книга не существует"

    def change_book(self, tittle, name_of_data, data):
        index = self.search_book_index(tittle)
        if index is not None:
            if name_of_data in BookList.book_list[index].keys():
                BookList.book_list[index][name_of_data] = data
                return f"{name_of_data} изменена на {data}"
            else:
                return "Такого значения нет"
        else:
            return "Изменяемая книга не существует"

    def search_book(self, tittle):
        index = self.search_book_index(tittle)
        if index is not None:
            return BookList.book_list[index]
        else:
            return "Искомая книга не существует"

    def save_to_json(self):
        with open(f"book_list.json", "w", encoding="utf-8") as fh:
            json.dump(BookList.book_list, fh, ensure_ascii=False, indent=2)
            return "Сохранено"

    def load_from_json(self):
        with open(f"book_list.json", "r", encoding="utf-8") as fh:
            BookList.book_list = json.load(fh)
            return "Загружено"
