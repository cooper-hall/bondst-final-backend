from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship

db = SQLAlchemy()
migrate = Migrate(db)


class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.String)
    active= db.Column(db.Boolean)
    receipt_items = db.relationship('Receipt_Item', backref='ticket', lazy=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __init__(self, sum, active):
        self.sum = sum
        self.active = active

    def to_dict(self):
        return{
            'id': self.id,
            'sum': self.sum,
            'active': self.active,
           }
    
    def receipt_items(self):
        return Receipt_Item.query.filter_by(order_id = self.id)
     
    def __repr__(self):
        return 'Tickets %r' % self.sum

class Receipt_Item(db.Model):
    __tablename__ = 'receipt_item'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String)
    ounces = db.Column(db.String)
    name = db.Column(db.String)
    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'ticket.id'), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, price, ounces, name, ticket_id):
        self.price = price
        self.ounces = ounces
        self.name = name
        self.ticket_id = ticket_id

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'ounces': self.ounces,
            'name': self.name,
            'ticket_id': self.ticket_id
        }
    
    def __repr__(self):
        return 'Receipt_Item %r' % self.name


class Drink(db.Model):
    __tablename__ = 'drink'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String)
    ounces = db.Column(db.String)
    name = db.Column(db.String)
    drinkType= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, price, ounces, name, drinkType):
        self.price = price
        self.ounces = ounces
        self.name = name
        self.drinkType = drinkType
    
    def to_dict(self):
        return{
        'id': self.id,
        'price': self.price,
        'name': self.name,
        'drinkType': self.drinkType
        }
    
    def __repr__(self):
        return 'Drink %r' % self.name

class Bottle(db.Model):
    __tablename__ = 'bottle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ounces = db.Column(db.String)
    price = db.Column(db.String)
    alcType = db.Column(db.String)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # drink_id = db.Column(db.Integer)

    def __init__(self, name, ounces, price, alcType, quantity):
        self.name = name
        self.ounces = ounces
        self.price = price
        self.alcType = alcType
        self.quantity = quantity

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        'ounces': self.ounces,
        'price': self.price,
        'alcType': self.alcType,
        'quantity': self.quantity
        }
    
    def __repr__(self):
        return 'Bottle %r' % self.name

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'password': self.password
        }
    
    def __repr__(self):
        return 'Employee %r' % self.name
    
