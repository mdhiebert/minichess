from minichess.games.abstract.piece import AbstractChessPiece
from minichess.games.gardner.action import GardnerChessAction


class AtomicChessAction(GardnerChessAction):
    '''
        A variant of chess where, on capture, all non-pawn pieces
        surrounding the captured piece are also removed.
    '''