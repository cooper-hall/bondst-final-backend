import os
# import redis
from datetime import timedelta
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

ACCESS_EXPIRES = timedelta(hours=12)

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
app.config["JWT_SECRET_KEY"] = 'time2beBONSTin2023foREEEAALLLL'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins='*')

# jwt_redis_blocklist = redis.StrictRedis(
#     host="localhost", port=6379, db=0, decode_responses=True
# )


# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     token_in_redis = jwt_redis_blocklist.get(jti)
#     return token_in_redis is not None


# @app.route("/logout", methods=["DELETE"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
#     return jsonify(msg="Access token revoked")


# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     return jsonify(hello="world")


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
    ticket = Ticket(data['sum'])
    db.session.add(ticket)
    db.session.commit()
    for item in data['items']:
        receipt_item = Receipt_Item(ticket.id, item['name'], item['price'], item['ounces'], item['quantity'])
        db.session.add(receipt_item)
        db.session.commit()
    return jsonify([i.to_dict() for i in ticket.receipt_items()]), 201

@app.patch('/update_ticket/<int:id>')
def update_ticket(id):
    data = request.json
    ticket = Ticket.query.get(id)
    for key, value in data.items():
        setattr(ticket, key, value)
    db.session.commit()
    return jsonify(ticket.to_dict()), 202

@app.delete('/delete_ticket/<int:id>')
def delete_ticket(id):
    ticket = Ticket.query.get(id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        return jsonify(ticket.to_dict), 200
    else:
        return {'error': 'No ticket found'}, 404
#receipt item routes#

@app.delete('/receipt_items/<int:id>')
def delete_receipt_item(id):
    item = Receipt_Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify(item), 200

@app.post('/create_receipt_item')
def receipt_item():
    data = request.json
    receipt_item = Receipt_Item(
        data['ticket_id'], data['name'], data['price'], data['ounces'], data['quantity'])
    db.session.add(receipt_item)
    db.session.commit()
    return jsonify(receipt_item.to_dict()), 201

@app.patch('/update_receipt_item')
def update_item():
    data = request.json
    rec_item = Receipt_Item.query.get(id)
    for key, value in data.items():
        setattr(rec_item, key, value)
    db.session.commit()
    return jsonify(rec_item.to_dict()), 202

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

@app.get('/bottles/<string:alcType>')
def bottle(alcType):
    bottles = Bottle.query.filter_by(alcType=alcType).all()
    if bottles:
        return jsonify([bottle.to_dict() for bottle in bottles])
    else:
        return {}, 404


@app.patch('/update_bottle/<int:id>')
def update_bottle(id):
    data = request.json
    bottle = Bottle.query.get(id)
    newOunces = bottle.ounces - data['ounces']
    bottle.ounces = newOunces
    if newOunces <= 0:
        bottle.ounces = 24 
        bottle.quantity -= 1
    db.session.commit()
    return jsonify(bottle.to_dict()), 202

#user routes#

@app.post('/employee_login')
def employee_login():
    data = request.json
    employee = Employee.query.filter_by(username=data['username']).first()
    if not employee:
        return jsonify({'error': 'no user found'}), 404
    else:
        given_password = data['password']
        if employee.password == given_password:
            # authenticate the employee
            token = create_access_token(identity=employee.id)
            return jsonify({'employee': employee.to_dict(), 'token': token})
        else:
            return jsonify({'error': 'invalid password'}), 422

@app.get('/which_employee')
@jwt_required()
def which_employee():
    current_employee = get_jwt_identity
    employee = Employee.query.get(current_employee)
    if employee:
        return jsonify(employee.to_dict()), 200
    else: 
        return jsonify({'error': 'you do not work here!'}), 404
    
@app.get('/employees')
def employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@app.post('/new_employee')
def new_employee():
    data = request.json
    new_employee = Employee(
        data['username'], data['password'], data['first_name'], data['last_name'], data['email'], data['phone'], data['address'], data['admin'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.to_dict()), 201

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
#     socketio.run(app, host='0.0.0.0', port=os.environ.get('PORT', 4000))
