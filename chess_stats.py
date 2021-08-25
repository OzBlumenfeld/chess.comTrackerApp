from cli_action import CliActionPerformer
from chess_utils import get_best_blitz_chess_stats, get_last_blitz_stats, get_blitz_chess_stats_record


class ChessProfileStats(CliActionPerformer):
    def execute_action(self):
        username = input("Enter username to check on:\n")

        best = get_best_blitz_chess_stats(username)
        last = get_last_blitz_stats(username)
        record = get_blitz_chess_stats_record(username)
        print(f'{username} best stats:\n{best}\n')
        print(f'{username} last stats:\n{last}\n')
        print(f'{username} record:\n{record}\n')

        won_games = record['win']
        lost_games = record['loss']
        draw_games = record['draw']
        total_games = won_games + lost_games + draw_games

        win_percentage = (won_games / total_games) * 100
        loss_percentage = (lost_games / total_games) * 100
        draw_percentage = (draw_games / total_games) * 100

        print(f'Win percentage: {win_percentage}%')
        print(f'Loss percentage: {loss_percentage}%')
        print(f'Draw percentage: {draw_percentage}%')
