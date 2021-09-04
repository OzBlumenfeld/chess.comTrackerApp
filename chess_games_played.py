from cli_action import CliActionPerformer
from chess_utils import get_user_monthly_games
from cli_utils import print_border_line


def validate_input(username, month, year):
    if not username:
        raise ValueError('Wrong username')
    if not month or len(month) != 2 or month.isnumeric() is False or int(month) > 12 or int(month) < 1:
        raise ValueError(f'Wrong input pattern month: {month}, input should be like: MM')
    if not year or len(year) != 4 or year.isnumeric() is False:
        raise ValueError(f'Wrong input pattern year: {year}, should be YYYY')


class ChessGamesPlayed(CliActionPerformer):
    def execute_action(self):
        try:
            username = input("Enter username to check on:\n")
            month = input("Enter a month in the following pattern MM:\n")
            year = input("Enter an year in the following pattern YYYY:\n")

            validate_input(username, month, year)

            games = get_user_monthly_games(username, month, year)
            number_of_games_this_month = len(games)
            print(f'{username} played at {month}/{year} {number_of_games_this_month} games\n')

        except Exception as e:
            print_border_line()
            print(f'Error occurred during input phase...\nError message: {e}')
            print_border_line()
