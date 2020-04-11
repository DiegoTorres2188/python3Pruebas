
from Password import Password
from Users import addUser, User


def CreateNewUser():
    name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")
    dni = input("Ingrese su número de DNI: ")

    user = User(dni, name, last_name)
    addUser(user)
    password = input("Ingrese una clave: ")
    password = Password(user.dni, password)
    Password.save(password)
    print("Usuario Creado")
    return


