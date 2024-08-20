from book_creator import CreateBookList


def librian_code():
    creator = CreateBookList()
    creator.load_from_json()
    interface = """Выберите:
        0 - Выход
        1 - Добавить книгу
        2 - Удалить книгу
        3 - Изменить данные книги
        4 - Поиск книги
        5 - Сохранить
        6 - Загрузить
    """
    choose = int(input(interface))
    while choose != 0:
        if choose in range(1, 7):
            if choose == 1:
                tittle = input("Введите название новой книги: ")
                year = input("Введите год книги: ")
                author = input("Введите автора книги: ")
                print(creator.create_book(tittle, year, author))
            elif choose == 2:
                tittle = input("Введите название книги которую нужно удалить: ")
                print(creator.remove_book(tittle))
            elif choose == 3:
                tittle = input("Введите название книги которую нужно изменить: ")
                if creator.search_book_index(tittle) is not None:
                    name_of_data = input("Введите что нужно изменить: ")
                    data = input("Значение: ")
                    print(creator.change_book(tittle, name_of_data, data))
                else:
                    print("Книга не найдена")
            elif choose == 4:
                tittle = input("Введите название книги которую нужно найти: ")
                result = creator.search_book(tittle)
                if result is not None:
                    print(f"---\ntittle: {result["tittle"]}\n"
                          f"year: {result["year"]}\n"
                          f"author: {result["author"]}\n---")
                else:
                    print("---\nИскомая книга не найдена\n---")
            elif choose == 5:
                print(creator.save_to_json())
            elif choose == 6:
                print(creator.load_from_json())
        else:
            print("Такого выбора нет")
        choose = int(input(interface))
