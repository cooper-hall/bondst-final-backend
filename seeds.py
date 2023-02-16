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
      drink10 = Drink('12.50', '3', 'BONDST Special', 'Special')
      drink11 = Drink('12.50', '3', 'Peach Milk Water', 'Special')
      drink12 = Drink('5.00', '6', 'Other', 'Other')
      bottle1 = Bottle("Hendrick's", '24', '5.50', 'Gin', 10)
      bottle2 = Bottle("Jack Daniels", '24', '5.50', 'Whiskey', 3)
      bottle3 = Bottle("Tito's Vodka", '24', '5.50', 'Vodka', 1)
      bottle4 = Bottle("Patrón", '24', '10.50', 'Tequila', 6)
      bottle5 = Bottle("Ki No Bi", '24', '8.50', 'Gin', 8)
      bottle6 = Bottle("Nikka Coffey Whiskey", '24', '8.50', 'Whiskey', 9)
      bottle7 = Bottle("Reyka", '24', '8.50', 'Vodka', 0)
      bottle8 = Bottle("Casamigos", '24', '10.50', 'Tequila', 3)
      bottle9 = Bottle("Monkey 47", '24', '10.50', 'Gin', 6)
      bottle10 = Bottle("Hibiki", '24', '10.50', 'Whiskey', 8)
      bottle11 = Bottle("Kastra Elion", '24', '10.50', 'Vodka', 7)
      bottle12 = Bottle("Don Julio 1942", '24', '12.50', 'Tequila', 4)
      bottle13 = Bottle("Roku", '24', '6.50', 'Gin', 2)
      bottle14 = Bottle("Balvenie 12", '24', '15.50', 'Whiskey', 10)
      bottle15 = Bottle("Haku", '24', '10.50', 'Vodka', 10)
      bottle16 = Bottle("Clase Azul", '24', '10.50', 'Tequila', 8)
      bottle17 = Bottle("Empress", '24', '5.50', 'Gin', 10)
      bottle18 = Bottle("Glenlivet 18", '24', '18.50', 'Whiskey', 7)
      bottle19 = Bottle("Salcombe Rosé",'24', '5.50', 'Gin', 2)
      bottle20 = Bottle("818 Tequila Añejo", '24', '10.50', 'Tequila', 8)
      bottle21 = Bottle("Arette Blanco", '24', '5.0', 'Tequila', 7)
      bottle22 = Bottle("Beefeater", '24', '5.50', 'Gin', 7)
      bottle23 = Bottle("Sông Cái", '24', '12.50', 'Gin', 2)
      bottle24 = Bottle("Calle 23 Reposado", '24', '13.25', 'Tequila', 3)
      bottle25 = Bottle("Yamazaki 12", '24', '18.50', 'Whiskey', 3)
      bottle26 = Bottle("Kikori", '24', '13.50', 'Whiskey', 5)
      bottle27 = Bottle("Boyd & Blair", '24', '11.75', 'Vodka', 7)
      bottle28 = Bottle("Barr Hill Tom Cat", '24', '11.25', 'Gin', 4)
      bottle29 = Bottle("Cotswolds Dry", '24', '10.50', 'Gin', 1)
      bottle30 = Bottle("Purity", '24', '7.50', 'Vodka', 2)
      employee1 = Employee("bradchad", "1111")
      employee2 = Employee("debra26", "2222")
      employee3 = Employee("brian43", "3333")
      db.session.add_all(
          [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9, drink10, drink11, drink12, bottle1, bottle2, bottle3, bottle4, bottle5, bottle6, bottle7, bottle8, bottle9, bottle10, bottle11, bottle12, bottle13, bottle14, bottle15, bottle16, bottle17, bottle18, bottle19, bottle20, bottle21, bottle22, bottle23, bottle24, bottle25, bottle26, bottle27, bottle28, bottle29, bottle30, employee1, employee2, employee3])
      db.session.commit()
      print('Done! :deciduous_tree:')

run_seeds()



