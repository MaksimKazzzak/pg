from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        # barva figurky ('white' nebo 'black')
        self.__color = color
        # pozice figurky na šachovnici (řádek, sloupec)
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        # každá figurka musí implementovat vlastní pohyby
        pass

    @staticmethod
    def is_position_on_board(position):
        # kontrola, zda je pozice na šachovnici
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        # pěšák postupuje pouze vpřed
        row, col = self.position
        moves = []

        # bílý → řádek +1, černý → řádek -1
        step = 1 if self.color == "white" else -1
        new_pos = (row + step, col)

        # pěšák nebere diagonálně, uvažujeme jen volný tah dopředu
        if self.is_position_on_board(new_pos):
            moves.append(new_pos)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position

        # L-tahy jezdce (8 možností)
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        # přidáme pouze ty tahy, které jsou na šachovnici
        return [m for m in moves if self.is_position_on_board(m)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        # střelec → pohyb pouze diagonálně, libovolný počet polí
        row, col = self.position
        moves = []

        # 4 diagonální směry
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8):  # maximálně 7 polí
                new_pos = (row + dr * i, col + dc * i)

                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    # zastavíme směr, pokud bychom vyšli mimo desku
                    break

        return moves  # ← opraveno, dříve chybělo (způsobovalo NoneType chybu)

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        # věž → pohybuje se pouze rovně (vertikálně, horizontálně)
        row, col = self.position
        moves = []

        # vertikální směry
        for i in range(1, 8):
            if self.is_position_on_board((row + i, col)):
                moves.append((row + i, col))
            if self.is_position_on_board((row - i, col)):
                moves.append((row - i, col))

        # horizontální směry
        for i in range(1, 8):
            if self.is_position_on_board((row, col + i)):
                moves.append((row, col + i))
            if self.is_position_on_board((row, col - i)):
                moves.append((row, col - i))

        # ← return musí být AŽ zde, ne uvnitř cyklu!
        # U tebe byl v původním kódu ve smyčce, což způsobilo,
        # že věž vrátila jen 1 krok doleva a doprava.
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        # dáma = kombinace věže + střelce
        row, col = self.position
        moves = []

        # všech 8 směrů
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),      # věžové směry
            (1, 1), (1, -1), (-1, 1), (-1, -1)     # diagonály
        ]

        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + dr * i, col + dc * i)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        # král → jeden krok do všech směrů
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'

    piece = Rook("white", (5, 5))
    print(piece)
    print(piece.possible_moves())
