import sqlite3


class Password:

    def __init__(self, userDni=None, password=None):
        self.userDni = userDni
        self.password = password

    def __str__(self):
        return "DNI: {} ==> Clave: {}".format(self.userDni, self.password)

    def save(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO passwords VALUES('{}','{}')".format(self.userDni, self.password))
        connection.commit()
        connection.close()
