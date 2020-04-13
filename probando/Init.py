import sqlite3


class Init:

    def __init__(self):
        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE options ('code' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' VARCHAR NOT NULL)")
            connection.commit()
            connection.close()
        except:
            pass

        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE users ('dni' VARCHAR PRIMARY KEY, 'name' VARCHAR NOT NULL, 'last_name' VARCHAR NOT NULL)")
            connection.commit()
            connection.close()
        except:
            pass

        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE passwords ('userDni' VARCHAR PRIMARY KEY, 'password' VARCHAR NOT NULL, FOREIGN KEY (userDni) REFERENCES users(dni))")
            connection.commit()
            connection.close()
        except:
            pass

        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE optionsAplication ('code' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' VARCHAR NOT NULL)")
            connection.commit()
            connection.close()
        except:
            pass
        #
        # try:
        #     connection = sqlite3.connect("prueba.db")
        #     cursor = connection.cursor()
        #     cursor.execute("DROP TABLE categories)")
        #     connection.commit()
        #     connection.close()
        # except:
        #     pass
        #
        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE categories ('id' VARCHAR PRIMARY KEY, 'name' VARCHAR NOT NULL)")
            connection.commit()
            connection.close()
        except:
            pass

        try:
            connection = sqlite3.connect("prueba.db")
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE dishes ('name' VARCHAR PRIMARY KEY, 'description' VARCHAR NOT NULL, 'price' VARCHAR NOT NULL, 'categoryId' VARCHAR NOT NULL, FOREIGN KEY (categoryId) REFERENCES categories(id))")
            connection.commit()
            connection.close()
        except:
            pass


Init()
