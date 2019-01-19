import sqlite3
from flask_restful import Resource
from flask_restful import reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def ejecutar(query):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        return cursor.execute(query)

    @classmethod
    def find_by_username(slef, username):
        query = "SELECT * FROM USERS WHERE username='{0}'".format(username)
        resultado = slef.ejecutar(query)
        row = resultado.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None

        return user

    @classmethod
    def find_by_id(self, id):
        query = "SELECT * FROM USERS WHERE id='{0}'".format(id)
        resultado = self.ejecutar(query)
        row = resultado.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None

        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='this is required')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='this is required')

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'mensage':"ests user ya est "},400
        
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "INSERT INTO users VALUES (NULL ,?,?)"
        cursor.execute(query, (data['username'], data['password']))
        connect.commit()
        connect.close()
        return {'message': "User create"}, 201
