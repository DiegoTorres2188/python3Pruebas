import sqlite3

from Category import Category, Categories, addCategory
from Dish import Dish, addDish


class OptionAplication():

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return "Opción {} ==> {}".format(self.code, self.name)


class AplicationOptions:
    options = []

    def __init__(self, userDni):
        self.userDni = userDni
        self.options = self.load()

    def load(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM optionsAplication")
        optionsDB = cursor.fetchall()
        if optionsDB == None:
            print("No hay opciones cargadas")
        else:
            for option in optionsDB:
                self.options.append(OptionAplication(option[0], option[1]))
            return self.options

    def showOptions(self):
        for o in self.options:
            print(o)

    def option(self, optionEntered):
        if optionEntered == "1":
            id = input("Ingrese un Id: ")
            name = input("Ingrese un nombre de Categoria: ")
            category = Category(id, name)
            addCategory(category)
            print("Se ha agregado la categoría")
        elif optionEntered == "2":
            categories = Categories()
            Categories.showAllCategories(categories)
        elif optionEntered == "3":
            categories = Categories()
            Categories.showAllCategories(categories)
            categoryId = input("Ingrese el Id de la categoría donde quiere ingresar el plato: ")
            name = input("Ingrese un nombre del Plato: ")
            description = input("Ingrese una descripción completa del plato: ")
            price = input("Ingrese el precio del plato: ")
            dish = Dish(name, description, price, categoryId)
            addDish(dish)
            print("Se ha agregado el plato {}.".format(name))
