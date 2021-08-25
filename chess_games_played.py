from cli_action import CliActionPerformer
from chess_utils import get_user_monthly_games

class ChessGamesPlayed(CliActionPerformer):
    def execute_action(self):
        username = input("Enter username to check on:\n")
        month = input("Enter a month in the following patten MM:\n")
        year = input("Enter an year in the following patten YYYY:\n")

        games = get_user_monthly_games(username, month, year)
        number_of_games_this_month = len(games)
        print(f'{username} played at {month}/{year} {number_of_games_this_month} games\n')

