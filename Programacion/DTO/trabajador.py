from DTO.persona import Persona

class Trabajador(Persona): # Trabajador heredara todo desde la clase Persona
    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.codigo_trabajador = ""

    def trabajar(self):
        print(f"{self.nombre} esta trabajando.")