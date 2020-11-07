from minichess.games.abstract.board import AbstractBoardStatus
from minichess.players.gardner import RandomPlayer
from minichess.games.gardner.board import GardnerChessBoard
from minichess.games.gardner.action import GardnerChessAction

if __name__ == "__main__":
    g = GardnerChessBoard()
    p = RandomPlayer()

    while g.status == AbstractBoardStatus.ONGOING:
        print(g)

        actions = g.legal_actions()

        # for action in actions:
        #     print(action)
        
        proposed = p.propose_action(g, None, g.legal_action_mask())

        input()
        proposed = GardnerChessAction.decode(proposed, g)
        g.push(proposed)

        print('+---------------+')

    print('***')
    # all_actions = g.legal_actions_for_color(g.active_color, filter_for_check=False)
    # for act in all_actions:
    #     print(act)

    print(g.status)



