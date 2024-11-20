from DAO.crudUsuario import registrar_usuario
from DTO.usuario import Usuario

print("REGISTRO DE USUARIO")
print("*******************")

nombre = input("Ingrese su nombre: ")
email = input("Ingrese su email: ")
password = input("Ingrese su contraseña: ")

usuario = Usuario()
usuario.nombre = nombre
usuario.set_email(email)
usuario.set_password(password)

registrar_usuario(usuario)

print("Usuario registrado.")