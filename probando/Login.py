import sqlite3

from AplicationOptions import AplicationOptions
from Password import Password




class Login:

    def __init__(self):
        self.userDni = input("Ingrese su numero de DNI: ")
        self.passwordEntered = input("Ingrese su contraseña: ")
        entryAplication = self.validate()
        if entryAplication == "access":
            print("Bienvenido")
            aplication = AplicationOptions(self.userDni)
            aplication.showOptions()
            optionEntered = input('''
            Elije tu opción: ''')
            aplication.option(optionEntered)
        elif entryAplication == "user not exist":
            print("No se ha podido encontrar el usuario")
        else:
            print("Contraseña incorrecta")
            pass

    def validate(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM passwords WHERE userDni = '{}'".format(self.userDni))
        registeredPassword = cursor.fetchone()

        if registeredPassword == None:
            return "user not exist"
        password = Password(registeredPassword[0],registeredPassword[1])
        if password.password == self.passwordEntered:
            return "access"
        else:
            return "denied"
