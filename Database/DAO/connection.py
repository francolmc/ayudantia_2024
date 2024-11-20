import pymysql

class Connection:
    def __init__(self, server: str, database: str, user: str, password: str) -> None:
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.__connection = None
        self.__cursor = None

    # Abrir conexion con bbdd
    def open(self):
        self.__connection = pymysql.connect(host=self.server, user=self.user, passwd=self.password, database=self.database)
        self.__cursor = self.__connection.cursor()

    # Ejecutar la operacion en la base de datos
    def execute(self, sql: str):
        self.__cursor.execute(sql)
        return self.__cursor
        

    # Asegurar que la operacion fue realizada
    def commit(self):
        self.__connection.commit()

    # Cerrar conexion con la base de datos
    def close(self):
        self.__connection.close()