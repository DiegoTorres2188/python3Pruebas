import sqlite3


class Dish:
    def __init__(self, name, description, price, categoryId):
        self.name = name
        self.description = description
        self.price = price
        self.categoryId = categoryId

    def __str__(self):
        return '''{}: ${}  ({})'''.format(self.name, self.price, self.description)


class Dishes:
    dihes = []

    def __init__(self):
        self.dihes = self.load()

    def showAllDishes(self):
        if len(self.dihes) == 0:
            print("No existen platos cargados")
        else:
            for p in self.dihes:
                print(p)

    def load(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dishes")
        dishesList = cursor.fetchall()
        self.dishes = []
        if len(dishesList) == 0:
            print("No hay platos cargados.")
        else:
            for d in dishesList:
                self.dishes.append(Dish(d[0], d[1], d[2], d[3]))
            return self.dihes


def addDish(dish):
    try:
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dishes VALUES('{}','{}','{}','{}')".format(dish.name, dish.description, dish.price,
                                                                               dish.categoryId))
        connection.commit()
        connection.close()
    except:
        return "No se puede agregar el plato"
