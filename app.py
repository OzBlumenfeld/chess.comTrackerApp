from flask import Flask
import db_connection

app = Flask(__name__)


# check how to turn on debug mode
@app.route("/")
def home_page():
    json = {'name': 'Oz'}
    coll = db_connection.getDbConnection('test', 'test')
    print(db_connection.findDocument(coll, json))
    # coll.insert_one({'name': 'Oz'})
    return 'fuck you !!!'

    # online_users = mongo.db.users.find({"online": True})
    # return render_template("index.html",
    #     online_users=online_users)

# def email_request():

# def main():
#     print('hi there!')


# if __name__ == "__main__":
#     # execute only if run as a script
#     main()