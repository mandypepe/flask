from flask import Flask,request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required
from security import *

app = Flask(__name__)
app.secret_key='lolo'
api = Api(app)
jwt=JWT(app,authenticate,identity)
items = []


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='no puede ser blanco')

    #@jwt_required
    def get(self,name):
        #item=list(filter(lambda x:x['name']==name,items)) #  lista todos los elementos filtrados
        print(items)
        item = next(filter(lambda x: x['name'] == name, items),None) # retorna el 1mer  element de la lista sino NONE
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404

    def post(self,name):
        data = Items.parser.parse_args()

        if next(filter(lambda x: x['name'] == name, items),None):
                return {'mensage':'El elemento {name} existe'.format(name=name)},404


        #data = request.get_json()
        print(data)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items=list(filter(lambda x: x['name']!=name,items))
        return {'mesage':'ITEM DOWN'}

    def put(self,name):
        data=Items.parser.parse_args()

        #data=request.get_json()
        item=next(filter(lambda x: x['name'] == name, items),None) # retorna el 1mer  element de la lista sino NONE
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Items,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(debug=True)
