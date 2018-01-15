from flask import Flask, request
from flask_restful import Resource, Api
import MySQLdb
from json import dumps
from flask.ext.jsonpify import jsonify


# Connect to the database.
db_connect = MySQLdb.connect(host="localhost",
    user="root",
    passwd="pw",
    db="scraper_db",
    charset="utf8",
    use_unicode=True,)

app = Flask(__name__)
api = Api(app)


# Class methods all follow a similar pattern:
# Connection to database is established, query is executed and (jsonified)
# results are returned.

# Return all contents.
class Contents(Resource):
    def get(self):
        conn = db_connect.cursor()
        query = conn.execute('SELECT * FROM contents')
        return {'contents': [i[0] for i in query.cursor.fetchall()]}


class Contents_Id(Resource):
    def get(self, content_id):
        conn = db_connect.cursor()
        query = conn.execute('SELECT * FROM contents WHERE id =%d ' % int(content_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

# Add data to db.
class Submit(Resource):
    def get(self):
        return 'get request was sent - no entry was made. Please use post.'
    def post(self):
        conn = db_connect.cursor()
        query = conn.execute('INSERT INTO contents(title, contents) VALUES (\'Super Headline\', \'This is some quality content here.\')')
        return 'POST REQUEST WAS SENT - database entry was added.'




api.add_resource(Contents, '/contents')
api.add_resource(Contents_Id, '/contents/<content_id>')
api.add_resource(Submit, '/submit') # Post to flask.

if __name__ == '__main__':
    app.run(port=5002)
