from minichess.games.atomic.pieces import Pawn
from minichess.games.abstract.action import AbstractActionFlags, AbstractChessAction
from minichess.games.gardner.board import GardnerChessBoard
from minichess.games.atomic.pieces import MultiPiece

class AtomicChessBoard(GardnerChessBoard):
    def push(self, action: AbstractChessAction, check_for_check=True):

        from_pos = action.from_pos
        to_pos = action.to_pos

        if check_for_check:
            checking_move, opp_cant_move = self._is_checking_action(action, self.active_color)

            if checking_move: action.modifier_flags.append(AbstractActionFlags.CHECK)
            if checking_move and opp_cant_move: action.modifier_flags.append(AbstractActionFlags.CHECKMATE)

        is_capture = AbstractActionFlags.CAPTURE in action.modifier_flags

        agent = self.get(from_pos).pop()

        if is_capture:
            pieces = []
            row, col = to_pos
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):

                    # captured pieces added to multipiece no matter what
                    if (i,j) == (row,col):
                        pieces.append(self.get((i,j)).pop())

                    else:
                        # valid position, occupied, not occupied by pawn
                        if 0 <= i < 5 and 0 <= j < 5 and self.get((i,j)).occupied() and type(self.get((i,j)).peek()) != Pawn: 
                            tile = self.get((i,j))
                            pieces.append(tile.pop())
                        else:
                            pieces.append(None)


            captured_piece = MultiPiece(pieces, to_pos, -1)

            action.captured_piece = captured_piece
        else:
            # otherwise move piece from A to B
            self.get(to_pos).push(agent)

        self.move_history.append(action)

        self.active_color = self.active_color.invert()

    def pop(self) -> AbstractChessAction:

        if len(self.move_history) == 0: return None

        action = self.move_history.pop()

        from_pos = action.from_pos
        to_pos = action.to_pos
        agent = action.agent
        captured_piece = action.captured_piece

        self.get(from_pos).pop()
        self.get(from_pos).push(agent)

        self.get(to_pos).pop()
        row,col = to_pos
        if captured_piece is not None:
            if type(captured_piece) == MultiPiece:
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        # captured pieces added to multipiece no matter what
                        if (i,j) == to_pos:
                            tile = self.get((i,j))
                            piece = captured_piece.pop()
                            tile.push(piece)
                            action.captured_piece = piece
                        else:
                            # valid position, occupied, not occupied by pawn
                            if 0 <= i < 5 and 0 <= j < 5: 
                                tile = self.get((i,j))
                                tile.push(captured_piece.pop())
                            else:
                                captured_piece.pop()
            else:
                self.get(to_pos).push(captured_piece)

        self.active_color = self.active_color.invert()

        return action