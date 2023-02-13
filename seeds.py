from app import app
from models import db, Drink, Bottle, Employee


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
      drink7 = Drink('9.50', '2', 'Martinez', 'Classic')
      drink8 = Drink('9.50', '2', 'Manhattan', 'Classic')
      drink9 = Drink('12.50', '3', 'Pandan Float', 'Special')
      drink10 = Drink('12.50', '3', 'BONST Special', 'Special')
      drink11 = Drink('12.50', '3', 'Peach Milk Water', 'Special')
      drink12 = Drink('5.00', '6', 'Other', 'Other')
      bottle1 = Bottle("Hendrick's", '24', '5.50', 'Gin', 10)
      bottle2 = Bottle("Jack Daniels", '24', '5.50', 'Whiskey', 3)
      bottle3 = Bottle("Tito's Vodka", '24', '5.50', 'Vodka', 1)
      bottle4 = Bottle("Ki No Bi", '24', '8.50', 'Gin', 8)
      bottle5 = Bottle("Nikka Coffey Whiskey", '24', '8.50', 'Whiskey', 9)
      bottle6 = Bottle("Reyka", '24', '8.50', 'Vodka', 0)
      bottle7 = Bottle("Monkey 47", '24', '10.50', 'Gin', 6)
      bottle8 = Bottle("Hibiki", '24', '10.50', 'Whiskey', 8)
      bottle9 = Bottle("Kastra Elion", '24', '10.50', 'Vodka', 7)
      bottle10 = Bottle("Roku", '24', '6.50', 'Gin', 2)
      bottle11 = Bottle("Balvenie 12", '24', '15.50', 'Whiskey', 10)
      bottle12 = Bottle("Haku", '24', '10.50', 'Vodka', 10)
      employee1 = Employee("bradchad", "1111")
      employee2 = Employee("debra26", "2222")
      employee3 = Employee("brian43", "3333")
      db.session.add_all(
          [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9, drink10, drink11, drink12, bottle1, bottle2, bottle3, bottle4, bottle5, bottle6, bottle7, bottle8, bottle9, bottle10, bottle11, bottle12, employee1, employee2, employee3])
      db.session.commit()
      print('Done! :deciduous_tree:')

run_seeds()



