from flask import Flask, render_template, request, Response, make_response
import db_connection

from chess_utils import get_last_blitz_stats

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


# @app.route('/chess')

@app.route("/stats")
def get_player_stats():
    user = request.args.get('user')
    # resp_body = get_last_blitz_stats(user)
    resp_headers = {'Access-Control-Allow-Origin': '*'}



    # response = Response(response=resp_body, status=200, headers=resp_headers)
    response = make_response(get_last_blitz_stats(user))
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
