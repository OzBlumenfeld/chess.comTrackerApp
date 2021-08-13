from flask import Flask
import db_connection

app = Flask(__name__)


# check how to turn on debug mode
@app.route("/oz")
def home_page():
    json = {'name': 'Oz'}
    coll = db_connection.getDbConnection('test', 'test')
    return db_connection.findDocument(coll, json)['name']

    # online_users = mongo.db.users.find({"online": True})
    # return render_template("index.html",
    #     online_users=online_users)

@app.route("/")
def email_request():
    return 'fuck you !!!'

# def main():
#     print('hi there!')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)