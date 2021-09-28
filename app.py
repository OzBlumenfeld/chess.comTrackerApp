from flask import Flask, request, make_response

import db_connection

from chess_utils import get_last_blitz_stats, get_user_monthly_games, get_user_details, get_blitz_chess_stats_record

app = Flask(__name__)


# check how to turn on debug mode
# @app.route("/oz")
# def home_page():
#     json = {'name': 'Oz'}
#     coll = db_connection.getDbConnection('test', 'test')
#     return db_connection.findDocument(coll, json)['name']

# online_users = mongo.db.users.find({"online": True})
# return render_template("index.html",
#     online_users=online_users)


@app.route('/chess/games')
def get_games():
    args = request.args
    month = args.get('month')
    user = args.get('user')
    year = args.get('year')

    games_data = get_user_monthly_games(user, month, year)
    body = {'gamesPlayed': len(games_data)}
    return body


@app.route("/chess/stats")
def get_player_stats():
    user = request.args.get('user')
    user_details = get_user_details(user)

    response_body = get_last_blitz_stats(user)

    try:
        response_body['avatar'] = user_details['avatar']
    except KeyError:
        print('No avatar available for this player')
        response_body['avatar'] = None

    country = user_details['country']

    response_body['country'] = country[len(country) - 2: len(country)]
    response_body['status'] = user_details['status']
    games_num = get_user_monthly_games(user, '09', '2021')
    response_body['games'] = len(games_num)

    record = get_blitz_chess_stats_record(user)
    won_games = record['win']
    lost_games = record['loss']
    draw_games = record['draw']
    total_games = won_games + lost_games + draw_games

    response_body['win_percentage'] = (won_games / total_games) * 100
    response_body['loss_percentage'] = (lost_games / total_games) * 100
    response_body['draw_percentage'] = (draw_games / total_games) * 100

    # print(f'debug oz: {response_body}')

    response = make_response(response_body)
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response


@app.route("/chess/stats/month")
def get_player_stats_month():
    user = request.args.get('user')
    # month should be like 09 for September
    month = request.args.get('month')
    year = request.args.get('year')

    user_details = get_user_details(user)

    response_body = get_last_blitz_stats(user)

    try:
        response_body['avatar'] = user_details['avatar']
    except KeyError:
        print('No avatar available for this player')
        response_body['avatar'] = None

    country = user_details['country']

    response_body['country'] = country[len(country) - 2: len(country)]
    response_body['status'] = user_details['status']

    games_num = get_user_monthly_games(user, month, year)
    response_body['games'] = len(games_num)

    record = get_blitz_chess_stats_record(user)
    won_games = record['win']
    lost_games = record['loss']
    draw_games = record['draw']
    total_games = won_games + lost_games + draw_games

    response_body['win_percentage'] = (won_games / total_games) * 100
    response_body['loss_percentage'] = (lost_games / total_games) * 100
    response_body['draw_percentage'] = (draw_games / total_games) * 100

    # print(f'debug oz: {response_body}')

    response = make_response(response_body)
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response


@app.route("/")
def email_request():
    return 'Welcome to my website'
    # serving = 'serving...'
    # return render_template('app.html', content=serving)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
