from DTO.usuario import Usuario
from DAO.connection import Connection

def registrar_usuario(usuario: Usuario) -> Usuario:
    # Crear consulta insert para registrar usuario
    sql = f"INSERT INTO usuario (nombre, email, password) VALUES ('{usuario.nombre}', '{usuario.get_email()}', '{usuario.get_password()}')"
    # Crear conexion y ejecutar consulta en base de datos
    connection = Connection("localhost", "ayudantia_db", "root", "masterdba")
    connection.open()
    connection.execute(sql)
    connection.commit()
    connection.close()
    # Retornar al usuario registrado
    return usuario