import sqlite3

from CreateNewUser import CreateNewUser
from Login import Login



class InitOptions:
    options = []

    def __init__(self):
        print('''Bienvenidos a la aplicación
        ''')
        self.options = self.load()
        self.showAllOptions()
        self.chosenOption = self.chosenOption()
        if self.chosenOption == "1":
            CreateNewUser()
        if self.chosenOption == "2":
            Login()
        else:
            print("Elija una opción valida.")

    def load(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM options")
        optionsList = cursor.fetchall()
        connection.close()
        for option in optionsList:
            option = Option(option[0], option[1])
            self.options.append(option)
        return self.options

    def showAllOptions(self):
        if len(self.options) == 0:
            print("No hay opciones que mostrar")
        else:
            for option in self.options:
                print(option)

    def chosenOption(self):
        self.chosenOption = input('''
        Elije tu opción: ''')
        return self.chosenOption


class Option:

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return ("Opción {} ==> {}".format(self.code, self.name))


InitOptions()



