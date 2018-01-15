from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
import MySQLdb
from json import dumps
from flask_jsonpify import jsonify


# Connect to the database.
db = MySQLdb.connect(host="localhost",
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
        cursor = db.cursor()
        query = cursor.execute('SELECT * FROM contents')
        data = cursor.fetchall()
        return jsonify(data)

# Specific content item by id.
class Contents_Id(Resource):
    def get(self, content_id):
        cursor = db.cursor()
        query = cursor.execute('SELECT * FROM contents WHERE id =%d ' % int(content_id))
        data = cursor.fetchall()
        return jsonify(data)

# Add data to db.
class Submit(Resource):
    def get(self):
        return 'get request was sent - no entry was made. Please use post.'
    def post(self):
        # Get POST data as JSon.
        # What about the mimetype?
        json_data = request.get_json(force=True)
        un = json_data['username']
        pw = json_data['password']
        return jsonify(u=un, p=pw)


        #cursor = db.cursor()
        #query = cursor.execute('INSERT INTO contents(title, contents) VALUES (\'Super Headline\', \'This is some quality content here.\')')
        #db.commit()
        #return 'POST REQUEST WAS SENT - database entry was added.'


api.add_resource(Contents, '/contents')
api.add_resource(Contents_Id, '/contents/<content_id>')
api.add_resource(Submit, '/submit') # Post to flask.

if __name__ == '__main__':
    app.run(port=5002)
