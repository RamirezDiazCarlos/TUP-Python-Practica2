import datetime

class Usuario:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.estado = True
        self.fecha_alta = datetime.datetime.now()
        self.fecha_baja = None

    def dar_baja(self):
        self.estado = False
        self.fecha_baja = datetime.datetime.now()

    def validar_credenciales(self, usuario, contrasena):
        return self.usuario == usuario and self.contrasena == contrasena and self.estado


"""# Ejemplo de uso
if __name__ == "__main__":
    # Crear un nuevo usuario
    nuevo_usuario = Usuario("usuario1", "contrasena123")

    # Simular dar de baja al usuario
    nuevo_usuario.dar_baja()

    # Validar credenciales
    usuario_ingresado = "usuario1"
    contrasena_ingresada = "contrasena123"
    if nuevo_usuario.validar_credenciales(usuario_ingresado, contrasena_ingresada):
        print("Credenciales válidas.")
    else:
        print("Credenciales inválidas.")"""