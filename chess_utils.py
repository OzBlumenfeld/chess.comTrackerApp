import requests

def get_blitz_chess_stats_record(username):
    response = requests.get(f'https://api.chess.com/pub/player/{username}/stats')
    return (response.json()['chess_blitz']['record'])


def get_best_blitz_chess_stats(username):
    response = requests.get(f'https://api.chess.com/pub/player/{username}/stats')
    return (response.json()['chess_blitz']['best'])


def get_last_blitz_stats(username):
    response = requests.get(f'https://api.chess.com/pub/player/{username}/stats')
    return (response.json()['chess_blitz']['last'])

def get_user_monthly_games(username, month, year):
    response = requests.get(f'https://api.chess.com/pub/player/{username}/games/{year}/{month}')
    return response.json()['games']


# Print my chess.com statistics
# user = os.environ['MY_USER']
# month = '08'
# previous_month = '07'
# year = '2021'
# games_this_month = get_user_monthly_games(user, year, month)
# games_previous_month = get_user_monthly_games(user, year, previous_month)

# number_of_games_this_month = len(games_this_month)
# number_of_games_last_month = len(games_previous_month)

# print(f'I played at {month}/{year} {number_of_games_this_month} games')
# print(f'I played at {previous_month}/{year} {number_of_games_last_month} games')

# best = get_best_blitz_chess_stats(user)
# last = get_last_blitz_stats(user)
# record = get_blitz_chess_stats_record(user)
# print(f'Your best stats:\n{best}\n')
# print(f'Your last stats:\n{last}\n')
# print(f'Your record:\n{record}\n')
#
# won_games = record['win']
# lost_games = record['loss']
# draw_games = record['draw']
# total_games = won_games + lost_games + draw_games
#
# win_percentage = (won_games / total_games) * 100
# loss_percentage = (lost_games / total_games) * 100
# draw_percentage = (draw_games / total_games) * 100
#
# print(f'Win percentage: {win_percentage}%')
# print(f'Loss percentage: {loss_percentage}%')
# print(f'Draw percentage: {draw_percentage}%')
