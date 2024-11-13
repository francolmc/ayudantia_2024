class Usuario:
    def __init__(self) -> None:
        self.__id = None
        self.__email = None
        self.nombre = None
        self.__password = None

    def set_id(self, id: int):
        self.__id = id

    def get_id(self) -> int:
        return self.__id
    
    def set_email(self, email: str):
        # Agregar validacion de correo electronico
        self.__email = email
    
    def get_email(self) -> str:
        return self.__email
    
    def set_password(self, password: str):
        # Agregar validacion para el tipo de contraseña
        self.__password = password

    def get_password(self) -> str:
        return self.__password