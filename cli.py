from chess_games_played import ChessGamesPlayed
from chess_stats import ChessProfileStats


def welcome(strategies):
    f = open("banner.txt", "r")
    print(f'{f.read()}\n\n')
    while True:
        choice = input(f'\n\nPlease choose the action you desire to preform:\n{options()}')
        strat = strategies[int(choice) -1]
        strat.execute_action()


def options():
    return '1. Get player\'s stats' \
           '\n2. How many games did player played for given month and year\n'


if __name__ == '__main__':
    strategies = [ChessProfileStats(), ChessGamesPlayed()]
    welcome(strategies)
