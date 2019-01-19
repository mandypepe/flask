from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import *
import sqlite3
import json


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='no puede ser blanco')

    def find_by_name(self, name):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "Select * from items where name='{0}'".format(name)
        result = cursor.execute(query)
        row = result.fetchone()
        connect.commit()
        connect.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return None

    def insert(self, item):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "INSERT INTO items VALUES ('{0}',{1})".format(item['name'], item['price'])
        cursor.execute(query)
        connect.commit()
        connect.close()

    def update(self,item):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "UPDATE items set price='{0}' WHeRE name={1}".format(item['name'], item['price'])
        cursor.execute(query)
        connect.commit()
        connect.close()

    # @jwt_required
    def get(self, name):
        try:
            item = self.find_by_name(name)
        except:
            return "{'message':'corre que exploto'}"
        if item:
            return item
        return {'message': 'ITEM not '}, 404

    def post(self, name):
        data = Items.parser.parse_args()

        if self.find_by_name(name):
            return {'mensage': 'El elemento {name} existe'.format(name=name)}, 404
        item = {'name': name, 'price': data['price']}
        try:
            self.insert(item)
        except:
            return "{'mesage': 'corre que exploto'}", 500

        return item, 201

    def delete(self, name):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "Delete FROM items WHERe name='{0}'".format(name)
        try:
            cursor.execute(query)
        except:
            return "{'message':'corre que exploto'}",500
        connect.commit()
        connect.close()

        return {'mesage': 'ITEM DOWN'}

    def put(self, name):
        data = Items.parser.parse_args()
        # data=request.get_json()
        try:
         item = self.find_by_name(name)
        except:
            return "{'message':'corre que exploto find '}", 500

        item_update= {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(item_update)
            except:
                return "{'message':'corre que exploto insert '}",500
        else:
            try:
                self.update(item_update)
            except:
                return "{'message':'corre que exploto update'}",500
        return item_update


class ItemList(Resource):
    def get(self):
        items=[]
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "Select * from items "
        result = cursor.execute(query)
        row = result.fetchall()
        for item in row :
            items.append({"name":item[0],'price':item[1]})
        connect.commit()
        connect.close()

        return {'items': items}
