class estudiante ():
    def __init__(self,matricula,nombre,apellido,edad,calificacion):
        self.matricula = matricula
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.calificacion = calificacion
        

    def setCalificacion (self,calificacion):
        self.calificacion.append(calificacion)
        

    def promedio (self):
        pass

    def __str__(self) -> str:
        pass


class estGrad (estudiante):
    def __init__(self, matricula, nombre, apellido, edad, fecha, tesis):
        super().__init__(matricula, nombre, apellido, edad)
        self.fecha = fecha
        self.tesis = tesis
    

    def chkGrad (self):
        pass

print ("")