from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

store = [{
    'name': 'mierda',
    'item': [{
        'name': 'My elemento',
        'praice': 12.58
    }]

}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])  # ,methods=['POST','GET']
def create_store():
    print(request.get_json())
    request_ndata=request.get_json()
    new_store={
        'item':[],
        'name': request_ndata['name']
   }
    store.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods=['GET'])  # ,methods=['POST','GET']
def get_store_name(name):
    for stores in store:
        if stores['name']==name:
            return jsonify(stores)
        return jsonify({'message':'NOSE ENCONTRO'})



@app.route('/store', methods=['GET'])  # ,methods=['POST','GET']
def get_store():
    return jsonify({'store':store}) #converting


@app.route('/store/<string:name>/item', methods=['POST'])  # ,methods=['POST','GET']
def create_item_store(name):

    reques_data=request.get_json()
    print(reques_data)
    for item in store :
        if item['name']==name:
            new_item={'name':reques_data['name'],'praice':reques_data['praice']
            }
            return jsonify(new_item)
    return jsonify({'message': 'NOSE ENCONTRO'})



@app.route('/store/<string:name>/item', methods=['GET'])  # ,methods=['POST','GET']
def get_item_storm(name):
    for stores in store:
        if stores['name']==name:
            return jsonify({'item':stores['item']})
        return jsonify({'message':'NOSE ENCONTRO'})


if __name__ == '__main__':
    app.run(port=5000)
