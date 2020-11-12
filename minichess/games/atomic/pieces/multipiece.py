from typing import Set
from minichess.games.abstract.piece import AbstractChessPiece, PieceColor
import numpy as np

class MultiPiece(AbstractChessPiece):
    def __init__(self, pieces: Set[AbstractChessPiece], position: tuple, value: int) -> None:
        super().__init__(PieceColor.WHITE, position, value)
        self.pieces = pieces

    def _onehot(self):
        return np.array([-1, 0, -1, 0, -1, 0])

    def push(self, piece):
        self.pieces.add(piece)

    def pop(self):
        return self.pieces.pop()

    def __len__(self):
        return len(self.pieces)

    def __iter__(self):
        for piece in self.pieces:
            yield piece

    def __str__(self):
        return '*'