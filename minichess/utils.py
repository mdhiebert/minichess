import numpy as np

def numpy_softmax(x):
    '''
        Basic numpy implementation of softmax over a 1-D vector.
    '''
    return np.exp(x) / sum(np.exp(x))

def surrounding_pieces(pos_tup, board, return_pos=False):
    row,col = pos_tup
    pieces = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):

            cur_pos = (i,j)
            if 0 <= i < 5 and 0 <= j < 5:
                piece = board.get(cur_pos).peek()
            else:
                piece = None

            if return_pos:
                pieces.append((piece, cur_pos))
            else:
                pieces.append(piece)

    return pieces