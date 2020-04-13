import sqlite3


class User:

    def __init__(self, dni, name, last_name):
        self.dni = dni
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return"{} ==> {}, {}.".format(self.dni, self.name, self.last_name)


class Users:
    users = []

    def __init__(self):
        self.users = self.load()

    def load(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        usersList = cursor.fetchall()
        if len(usersList) == 0:
            print("No hay usuarios cargados.")
        else:
            for user in usersList:
                self.users.append(User(user[0], user[1], user[2]))
            return self.users

    def __str__(self):
        for u in self.users:
            print(u)


def addUser(user):
    try:
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES('{}','{}','{}')".format(user.dni, user.name, user.last_name))
        connection.commit()
        connection.close()
    except:
        print("No se pudo agregar el usuario")
