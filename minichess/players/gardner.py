from minichess.utils import numpy_softmax
import numpy as np
from minichess.players.abstract import Player

class RandomPlayer(Player):
    def __init__(self):
        super().__init__(1225)

    def propose_action(self, board, color, action_mask):

        action_weights = np.random.rand(self.action_space_size)

        legal_actions = action_weights * action_mask

        if np.all(legal_actions == 0): return False, None

        renormalized = numpy_softmax(legal_actions)

        idx = np.argmax(renormalized)

        action_vector = np.zeros(self.action_space_size)
        action_vector[idx] = 1

        action = GardnerChessAction.decode(action_vector, self.board)

        return True, action