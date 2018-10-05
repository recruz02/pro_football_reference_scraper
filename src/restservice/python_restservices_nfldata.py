#postgresql imports
import psycopg2
from connect import executeselect


#flask imports
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)
		

class Nflplayers(Resource):
    def get(self):
        query = executeselect("select nflplayerid, first_name, last_name, player_position, pro_football_reference_url from nflplayer where player_position = 'QB';","")

        row_headers= ['nflplayerid', 'first_name', 'last_name', 'player_position', 'pro_football_reference_url']
        json_data=[]
        for result in query:
            json_data.append(dict(zip(row_headers,result)))
            
        return jsonify(json_data)
 
		
"""
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        
api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
"""

api.add_resource(Nflplayers, '/nflplayers') # Route_1
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
     app.run(port='5002')
