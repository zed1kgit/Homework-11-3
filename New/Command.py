from __future__ import annotations
from abc import ABC, abstractmethod
from Pasta import PastaConcreteCreator1, PastaConcreteCreator2, PastaConcreteCreator3, PastaCreator


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class ShowPastaCommand(Command):
    def __init__(self, pasta_creator: PastaCreator):
        self._pasta = pasta_creator

    def execute(self):
        print(self._pasta.show_pasta())


if __name__ == "__main__":
    ShowPastaCommand(PastaConcreteCreator1()).execute()
    print("\n")

    ShowPastaCommand(PastaConcreteCreator2()).execute()
    print("\n")

    ShowPastaCommand(PastaConcreteCreator3()).execute()
    print("\n")
