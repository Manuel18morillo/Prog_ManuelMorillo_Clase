class Estudiante:
    def __init__(self, cedula, nombre, apellido, correo, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def Obtener_Estudiante(self):
        print("\nMi cédula es:", self.cedula , "\nMi nombre es:", self.nombre , "\nMi apellido es:", self.apellido , "\nMi correo es:", self.correo , "\nMi teléfono es:", self.telefono )
        
e = Estudiante("1234567890", "Manuel", "Morillo", "morillomanuel502@gmail.com", "3009813543")

e.Obtener_Estudiante()
    
    


