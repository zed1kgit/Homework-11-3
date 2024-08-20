from book_creator import CreateBookList


def reader_code():
    creator = CreateBookList()
    creator.load_from_json()
    interface = """Выберите:
    0 - Выход
    1 - Поиск книги
"""
    choose = int(input(interface))
    while choose != 0:
        if choose in range(1, 2):
            if choose == 1:
                tittle = input("Введите название книги которую нужно найти: ")
                result = creator.search_book(tittle)
                if result is not None:
                    print(f"---\nНазвание: {result["tittle"]}\n"
                          f"Год: {result["year"]}\n"
                          f"Автор: {result["author"]}\n---")
                else:
                    print("---\nИскомая книга не найдена\n---")
        else:
            print("Такого выбора нет")
        choose = int(input(interface))
