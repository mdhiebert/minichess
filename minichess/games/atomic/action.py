from typing import List
from minichess.games.abstract.action import AbstractActionFlags, AbstractChessAction, visitor
from minichess.games.abstract.piece import AbstractChessPiece
from minichess.games.gardner.action import GardnerChessAction, GardnerChessActionVisitor
from minichess.games.atomic.pieces import King


class AtomicChessAction(GardnerChessAction):
    '''
        A variant of chess where, on capture, all non-pawn pieces
        surrounding the captured piece are also removed.
    '''
    pass

class AtomicChessActionVisitor(GardnerChessActionVisitor):
    @visitor(King)
    def visit(self, piece: AbstractChessPiece, board) -> List[AbstractChessAction]:
        moves = super().visit(piece, board)

        return [move for move in moves if AbstractActionFlags.CAPTURE not in move.modifier_flags]