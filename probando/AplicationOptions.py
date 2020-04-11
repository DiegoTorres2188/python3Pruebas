import sqlite3

from Category import Category, Categories


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
            category = Category()
            categories = Categories()
            categories.addCategory(category)
            print("Se ha agregado la categoría")
        if optionEntered == "2":
            pass
