from Pasta import PastaConcreteCreator1, PastaConcreteCreator2, PastaConcreteCreator3, PastaCreator


def client_code(creator: PastaCreator) -> None:
    print(creator.show_pasta())


if __name__ == "__main__":
    client_code(PastaConcreteCreator1())
    print("\n")

    client_code(PastaConcreteCreator2())
    print("\n")

    client_code(PastaConcreteCreator3())
    print("\n")