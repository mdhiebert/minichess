from minichess.games.dark.board import DarkChessBoard
from minichess.games.rifle.board import RifleChessBoard
from minichess.games.abstract.board import AbstractBoardStatus
from minichess.players.gardner import RandomPlayer
from minichess.games.gardner.board import GardnerChessBoard
from minichess.games.gardner.action import GardnerChessAction

if __name__ == "__main__":
    # g = GardnerChessBoard()
    r = RifleChessBoard()
    d = DarkChessBoard()
    p = RandomPlayer()

    game = d

    while game.status == AbstractBoardStatus.ONGOING:
        print(game)
        # print(game.no_fog_board())

        actions = game.legal_actions()

        # for action in actions:
        #     print(action)
        
        proposed = p.propose_action(game, None, game.legal_action_mask())
        print(game.state_vector())

        input()
        proposed = GardnerChessAction.decode(proposed, game)
        game.push(proposed)

        print('+---------------+')

    print(game)

    print(game.status)



