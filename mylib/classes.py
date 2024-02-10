
class estudiante():
    def __init__(self, Matricula, Nombre, Edad, Cal1=None, Cal2=None, Cal3=None, Cal4=None, Cal5=None,final=None ):
        self.matricula = Matricula
        self.nombre= Nombre
        self.edad = Edad
        self.final = final
        self.cal1 = Cal1
        self.cal2 = Cal2
        self.cal3 = Cal3
        self.cal4 = Cal4
        self.cal5 = Cal5
        pass

    def __str__(self):
       return f"Matricula: {self.matricula}   Nombre: {self.nombre}     Edad: {self.edad} "  
    
    

class alumGrad(estudiante):
    def __init__(self, Matricula=None, Nombre=None, Edad=None, Cal1=None, Cal2=None, Cal3=None, Cal4=None, Cal5=None,final=None, fecha=None, tesis=None ):
        super().__init__(Matricula, Nombre, Edad, Cal1, Cal2, Cal3, Cal4, Cal5,final)
        self.fecha = fecha
        self.tesis = tesis
        pass
    
    def gradAlum (self):
        if self.final <= 5.9:
            return 'NO'
        else:
            return 'SI'
        
    def fechaGrad (self,fecha):
        self.fecha = fecha
        
    def tesisGrad (self,tesis):
        self.tesis = tesis
        