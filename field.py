import random

class Field:
    """
    Classe que representa o campo de batalha de cada jogador
    """
    def __init__(self):
        self._field = [['-' for j in range(9)] for i in range(9)]
        self.ships = 0

    def check_pos(self, coordinate:tuple, action:str) -> bool:
        """
        Recebe uma tupla da posição (letra, número) e uma ação e
        retorna se a ação pode ou não ser realizada.

        :param coordinate: tuple (letra, número)
        :param action: str 'add' ou 'remove'
        """
        x, y = coordinate
        # add
        if action == 'add':
            if self._field[x][y] == '-':
                return True
            else:
                return False
        # rmv
        else:
            if self._field[x][y] in ('o', '-'):
                return True
            else:
                return False

    def add(self, coordinate:tuple) -> None:
        """Adiciona um barco"""
        x, y = coordinate[0], coordinate[1]
        self._field[x][y] = 'o'
        self.ships += 1

    def remove(self, coordinate:tuple) -> None:
        """Remove um barco"""
        x, y = coordinate[0], coordinate[1]
        if self._field[x][y] == 'o':
            self._field[x][y] = 'x'
            self.ships -= 1
        else:
            self._field[x][y] = '~'
    @property   
    def show(self) -> list:
        return self._field

    @property
    def unshow(self) -> list:
        field = self._field[:]
        for y in field:
            for x in y:
                if x == 'o':
                    field[y][x] = '-'
        return field