import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, Ticket, Receipt_Item, Drink, Bottle, Employee
import platform
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, emit
import sys


app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.get('/')
def home():
    return send_file('welcome.html')

@app.get('/example')
def example():
    return {'message': 'Your app is running python'}

#ticket routes#

@app.get('/tickets')
def tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in tickets])

@app.post('/ticket')
def ticket():
    data = request.json 
    ticket = Ticket(data['sum'], data['active'])
    db.session.add(ticket)
    db.session.commit()
    for item in data['items']:
        receipt_item = Receipt_Item(ticket.id, item['name'], item['price'])
        db.session.add(receipt_item)
        db.session.commit()
    return jsonify([i.to_dict() for i in ticket.receipt_items()]), 201

@app.patch('/update_ticket')
def update_ticket():
    data = request.json
    ticket = Ticket.query.get(id)
    for key, value in data.items():
        setattr(ticket, key, value)
    db.session.commit()
    return jsonify(ticket.to_dict()), 202

#receipt item routes#

@app.delete('/receipt_items/<int: id >')
def delete_receipt_item():
    item = Receipt_Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify(item), 200

@app.post('/create_receipt_item')
def receipt_item():
    data = request.json
    receipt_item = Receipt_Item(data['price'], data['ounces'], data['name'], data['ticket_id'])
    db.session.add(receipt_item)
    db.session.commit()
    return jsonify(receipt_item.to_dict()), 201

#cocktail routes#

@app.get('/cocktails')
def cocktails():
    cocktails = Drink.query.all()
    return jsonify([cocktail.to_dict() for cocktail in cocktails])

#bottle routes#

@app.get('/bottles')
def bottles():
    bottles = Bottle.query.all()
    return jsonify([bottle.to_dict() for bottle in bottles])


# @app.post('/add_item_to_ticket')
# def add_item_to_ticket():
#     data = request.json
#     item
#     # get the selected item's info
#     # create it
#     # save it to the DB
#     # return the created item as json to the client
#     # on the client, update the UI/state, etc
#     pass


# @socketio.on('connect')
# def connected():
#     '''This function is an event listener that gets called when the client connects to the server'''
#     print(f'Client {request.sid} has connected')
#     emit('connect', {'data': f'id: {request.sid} is connected'})


# @socketio.on('data')
# def handle_message(data):
#     '''This function runs whenever a client sends a socket message to be broadcast'''
#     print(f'Message from Client {request.sid} : ', data)
#     emit('data', {'data': 'data', 'id': request.sid}, broadcast=True)


# @socketio.on("disconnect")
# def disconnected():
#     '''This function is an event listener that gets called when the client disconnects from the server'''
#     print(f'Client {request.sid} has disconnected')
#     emit('disconnect',
#          f'Client {request.sid} has disconnected', broadcast=True)


# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=os.environ.get('PORT', 3000))
