from librarian import librian_code
from reader import reader_code

if __name__ == "__main__":
    user = input("Введите пользователя: ")
    if user == "librarian":
        librian_code()
    else:
        reader_code()
