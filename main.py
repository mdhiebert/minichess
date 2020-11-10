from minichess.games.rifle.board import RifleChessBoard
from minichess.games.abstract.board import AbstractBoardStatus
from minichess.players.gardner import RandomPlayer
from minichess.games.gardner.board import GardnerChessBoard
from minichess.games.gardner.action import GardnerChessAction

if __name__ == "__main__":
    # g = GardnerChessBoard()
    r = RifleChessBoard()
    p = RandomPlayer()

    game = r

    while game.status == AbstractBoardStatus.ONGOING:
        print(game)

        actions = game.legal_actions()

        # for action in actions:
        #     print(action)
        
        proposed = p.propose_action(game, None, game.legal_action_mask())

        input()
        proposed = GardnerChessAction.decode(proposed, game)
        game.push(proposed)

        print('+---------------+')

    print(game)

    print(game.status)



