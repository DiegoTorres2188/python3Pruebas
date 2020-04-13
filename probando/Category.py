import sqlite3


class Category:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Id: {} >>>>> Nombre: {}".format(self.id, self.name)


class Categories:
    categories: []

    def __init__(self):
        self.categories = self.load()

    def showAllCategories(self):
        if len(self.categories) == 0:
            print("No existen categorías cargadas")
        else:
            for c in self.categories:
                print(c)

    def load(self):
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categories")
        categoriesList = cursor.fetchall()
        self.categories=[]
        if len(categoriesList) == 0:
            print("No hay usuarios cargados.")
        else:
            for c in categoriesList:
                self.categories.append(Category(c[0], c[1]))
            return self.categories

def addCategory(category):
    try:
        connection = sqlite3.connect("prueba.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO categories VALUES('{}','{}')".format(category.id, category.name))
        connection.commit()
        connection.close()
    except:
        return "No se puede agregar la categoria"
