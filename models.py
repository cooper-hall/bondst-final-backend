from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship

db = SQLAlchemy()
migrate = Migrate(db)


class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Float)
    # active= db.Column(db.Boolean)
    receipt_items = db.relationship('Receipt_Item', backref='ticket', lazy=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __init__(self, sum):
        self.sum = sum

    def to_dict(self):
        return{
            'id': self.id,
            'sum': self.sum
           }
    
    def receipt_items(self):
        return Receipt_Item.query.filter_by(ticket_id = self.id)
     
    def __repr__(self):
        return 'Tickets %r' % self.sum

class Receipt_Item(db.Model):
    __tablename__ = 'receipt_item'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    ounces = db.Column(db.Float)
    name = db.Column(db.String)
    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'ticket.id'), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, ticket_id, name, price) :
        self.ticket_id = ticket_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'ounces': self.ounces,
            'name': self.name,
            'ticket_id': self.ticket_id
        }

    def ticket(self):
        return Ticket.query.get(self.ticket_id)
    
    def __repr__(self):
        return 'Receipt_Item %r' % self.name


class Drink(db.Model):
    __tablename__ = 'drink'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    ounces = db.Column(db.Float)
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
    ounces = db.Column(db.Float)
    price = db.Column(db.Float)
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
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
    
    def __repr__(self):
        return 'Employee %r' % self.username
    
