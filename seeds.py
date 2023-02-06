from app import app
from models import db, Drink


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
      db.session.add_all(
          [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9])
      db.session.commit()
      print('Done! :deciduous_tree:')

run_seeds()



