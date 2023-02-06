from app import app
from models import db, Drink, Bottle


def run_seeds():
    print('Seeding database ... :seedling:')
# Add your seed data
    with app.app_context():
      drink1= Drink('7.50', '2', 'Gin & Tonic', 'Classic')
      drink2 = Drink('7.50', '2', 'Whiskey Sour', 'Classic')
      drink3 = Drink('7.50', '2', 'Vodka Soda', 'Classic')
      drink4 = Drink('9.50', '1.5', 'Negroni', 'Classic')
      drink5 = Drink('9.50', '2', 'Old Fashioned', 'Classic')
      drink6 = Drink('9.50', '2', 'Cosmo', 'Classic')
      drink7 = Drink('12.50', '3', 'BONST Special', 'Special')
      drink8 = Drink('12.50', '3', 'Peach Milk Water', 'Special')
      drink9 = Drink('5.00', '6', 'Other', 'Other')
      bottle1 = Bottle("Hendrick's", '2', '5.50', 'Gin', 10)
      bottle2 = Bottle("Ki No Bi", '2', '8.50', 'Gin', 10)
      bottle3 = Bottle("Monkey 47", '2', '10.50', 'Gin', 10)
      bottle4 = Bottle("Jack Daniels", '2', '5.50', 'Whiskey', 10)
      bottle5 = Bottle("Nikka Coffey Whiskey", '2', '8.50', 'Whiskey', 10)
      bottle6 = Bottle("Hibiki", '2', '10.50', 'Whiskey', 10)
      bottle7 = Bottle("Tito's Vodka", '2', '5.50', 'Vodka', 10)
      bottle8 = Bottle("Reyka", '2', '8.50', 'Vodka', 10)
      bottle9 = Bottle("Kastra Elion", '2', '10.50', 'Vodka', 10)

      db.session.add_all(
          [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9, bottle1, bottle2, bottle3, bottle4, bottle5, bottle6, bottle7, bottle8, bottle9])
      db.session.commit()
      print('Done! :deciduous_tree:')

run_seeds()



