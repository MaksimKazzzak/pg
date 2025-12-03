from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.

        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    def check_moves(self, moves):
        return [move for move in moves if self.is_position_on_board(move)]

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        moves = []
        row, col = self.position
        if self.color == 'white':
            new_pos = (row + 1, col)
        else:  # black
            new_pos = (row - 1, col)
        if self.is_position_on_board(new_pos):
            moves.append(new_pos)
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = self.check_moves(moves)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            for i in range(1, 8):
                new_row = row + dr * i
                new_col = col + dc * i
                new_position = (new_row, new_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            # upward
            if self.is_position_on_board((row + i, col)):
                moves.append((row + i, col))
            # backward
            if self.is_position_on_board((row - i, col)):
                moves.append((row - i, col))

        for i in range(1, 8):
            # Right
            if self.is_position_on_board((row, col + i)):
                moves.append((row, col + i))
            # Left
            if self.is_position_on_board((row, col - i)):
                moves.append((row, col - i))
            return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position  # Současná pozice královny
        moves = []
        # Seznam všech směrů (včetně diagonál, vertikál a horizontál)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertikální a horizontální směr
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonální směry
        ]
       # Generování pohybů pro každý směr
        for dr, dc in directions:
            for i in range(1, 8):  # Maximální počet buněk
                new_row = row + dr * i
                new_col = col + dc * i
                new_position = (new_row, new_col)

                if self.is_position_on_board(new_position):  # Kontrola hranic desky
                    moves.append(new_position)
                else:
                    break  # Přerušte smyčku, pokud překročíme hrací plochu
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
   # Téměř jako královna, ale bez nutnosti opakovat celé pole.
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertikální a horizontální směr
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonální směry
        ]
        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Rook("white", (5, 5))
    print(piece)
    print(piece.possible_moves())
