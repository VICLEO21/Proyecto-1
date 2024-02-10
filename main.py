from myLib import *

arr1 = [10,9,8,10,9]
Estudiante1 = estudiante(601049, "Zaira Acosta    ",35, )
Estudiante1.cal1 = arr1 [0]
Estudiante1.cal2 = arr1 [1] 
Estudiante1.cal3 = arr1 [2]
Estudiante1.cal4 = arr1 [3]
Estudiante1.cal5 = arr1 [4]
Estudiante1.final = sum(arr1)/5
Estudiante12 = alumGrad()
Estudiante12.fecha =("1/7/13")
Estudiante12.tesis = ("Los neutrinos saben a jugo de Uva.")



arr2 = [6,5,5,4,3]
Estudiante2 = estudiante(601048, "Durán Acosta    ",34 )
Estudiante2.cal1 = arr2 [0]
Estudiante2.cal2 = arr2 [1]
Estudiante2.cal3 = arr2 [2]
Estudiante2.cal4 = arr2 [3]
Estudiante2.cal5 = arr2 [4]
Estudiante2.final = sum(arr2)/5
Estudiante22 = alumGrad()
Estudiante22.fecha =("N/A")
Estudiante22.tesis = ("N/A")



arr3 = [8,3,4,5,4]
Estudiante3 = estudiante(100738, "García Victor   ",20 )
Estudiante3.cal1 = arr3 [0]
Estudiante3.cal2 = arr3 [1]
Estudiante3.cal3 = arr3 [2]
Estudiante3.cal4 = arr3 [3]
Estudiante3.cal5 = arr3 [4]
Estudiante3.final = sum(arr3)/5
Estudiante32 = alumGrad()
Estudiante32.fecha =("N/A")
Estudiante32.tesis = ("N/A")




arr4 = [10,9,8,10,8]
Estudiante4 = estudiante(100744, "López Diego     ",20 )
Estudiante4.cal1 = arr4 [0]
Estudiante4.cal2 = arr4 [1]
Estudiante4.cal3 = arr4 [2]
Estudiante4.cal4 = arr4 [3]
Estudiante4.cal5 = arr4 [4]
Estudiante4.final = sum(arr4)/5
Estudiante42 = alumGrad()
Estudiante42.fecha =("1/5/26")
Estudiante42.tesis = ("Análisis Actuarial del impacto económico de Pandemias en el sector asegurador.")



arr5 = [10,8,9,5,9] 
Estudiante5 = estudiante(100692, "López Evelyn    ",20)
Estudiante5.cal1 = arr5 [0]
Estudiante5.cal2 = arr5 [1]
Estudiante5.cal3 = arr5 [2]
Estudiante5.cal4 = arr5 [3]
Estudiante5.cal5 = arr5 [4]
Estudiante5.final = sum(arr5)/5
Estudiante52 = alumGrad()
Estudiante52.fecha =("1/5/27")
Estudiante52.tesis = ("Explorando la intersección entre Tecnología y Arquitectura.")



arr6 = [6,5,4,4,3]
Estudiante6 = estudiante(-99999, "Rojas Daniel    ",20)
Estudiante6.cal1 = arr6 [0]
Estudiante6.cal2 = arr6 [1]
Estudiante6.cal3 = arr6 [2]
Estudiante6.cal4 = arr6 [3]
Estudiante6.cal5 = arr6 [4]
Estudiante6.final = sum(arr6)/5
Estudiante62 = alumGrad()
Estudiante62.fecha =("N/A")
Estudiante62.tesis = ("N/A")



arr7 = [10,6,10,9,8]
Estudiante7 = estudiante(100870, "Rosas Maurizio  ",20)
Estudiante7.cal1 = arr7 [0]
Estudiante7.cal2 = arr7 [1]
Estudiante7.cal3 = arr7 [2]
Estudiante7.cal4 = arr7 [3]
Estudiante7.cal5 = arr7 [4]
Estudiante7.final = sum(arr7)/5
Estudiante72 = alumGrad()
Estudiante72.fecha =("1/8/26")
Estudiante72.tesis = ("Análisis predictivo en Big Data.")



arr8 = [10,5,7,8,10]
Estudiante8 = estudiante(100437, "Villegas Annibal",20)
Estudiante8.cal1 = arr8 [0]
Estudiante8.cal2 = arr8 [1]
Estudiante8.cal3 = arr8 [2]
Estudiante8.cal4 = arr8 [3]
Estudiante8.cal5 = arr8 [4]
Estudiante8.final = sum(arr8)/5
Estudiante82 = alumGrad()
Estudiante82.fecha =("1/12/26")
Estudiante82.tesis = ("Análisis táctico y estratégico en el Fútbol Moderno")


print ("\033[42mCalificaciones de estudiantes de actuaría UTEC\033[0m")
print("")
print ("                                         |        CALIFICACIONES       |                \n"+"Matricula |       Nombre      |   Edad   |  1  |  2  |  3  |  4  |  5  | Final | Grad ? | Fecha | Tesis | \n"+"-----------------------------------------------------------------------------------------------------------------------------")
print ((str(Estudiante1.matricula)+ "      " + (Estudiante1.nombre)+"    "+ str((Estudiante1.edad))+"         "+str(Estudiante1.cal1)+"     "+str(Estudiante1.cal2)+"     "+str(Estudiante1.cal3)+"    "+str(Estudiante1.cal4)+"     "+str(Estudiante1.cal5)+"    "+str(Estudiante1.final)+"     SI       "+ Estudiante12.fecha +"  "+ Estudiante12.tesis))
print ((str(Estudiante2.matricula)+ "      " + (Estudiante2.nombre)+"    "+ str((Estudiante2.edad))+"          "+str(Estudiante2.cal1)+"     "+str(Estudiante2.cal2)+"     "+str(Estudiante2.cal3)+"     "+str(Estudiante2.cal4)+"     "+str(Estudiante2.cal5)+"    "+str(Estudiante2.final)+"     NO       "+ Estudiante22.fecha +"     "+ Estudiante22.tesis))
print ((str(Estudiante3.matricula)+ "      " + (Estudiante3.nombre)+"    "+ str((Estudiante3.edad))+"          "+str(Estudiante3.cal1)+"     "+str(Estudiante3.cal2)+"     "+str(Estudiante3.cal3)+"     "+str(Estudiante3.cal4)+"     "+str(Estudiante3.cal5)+"    "+str(Estudiante3.final)+"     NO       "+ Estudiante32.fecha +"     "+ Estudiante32.tesis))
print ((str(Estudiante4.matricula)+ "      " + (Estudiante4.nombre)+"    "+ str((Estudiante4.edad))+"         "+str(Estudiante4.cal1)+"     "+str(Estudiante4.cal2)+"     "+str(Estudiante4.cal3)+"    "+str(Estudiante4.cal4)+"     "+str(Estudiante4.cal5)+"    "+str(Estudiante4.final)+"     SI       "+ Estudiante42.fecha +"  "+ Estudiante42.tesis))
print ((str(Estudiante5.matricula)+ "      " + (Estudiante5.nombre)+"    "+ str((Estudiante5.edad))+"         "+str(Estudiante5.cal1)+"     "+str(Estudiante5.cal2)+"     "+str(Estudiante5.cal3)+"     "+str(Estudiante5.cal4)+"     "+str(Estudiante5.cal5)+"    "+str(Estudiante5.final)+"     SI       "+ Estudiante52.fecha +"  "+ Estudiante52.tesis))
print ((str(Estudiante6.matricula)+ "      " + (Estudiante6.nombre)+"    "+ str((Estudiante6.edad))+"          "+str(Estudiante6.cal1)+"     "+str(Estudiante6.cal2)+"     "+str(Estudiante6.cal3)+"     "+str(Estudiante6.cal4)+"     "+str(Estudiante6.cal5)+"    "+str(Estudiante6.final)+"     NO       "+ Estudiante62.fecha +"     "+ Estudiante62.tesis))
print ((str(Estudiante7.matricula)+ "      " + (Estudiante7.nombre)+"    "+ str((Estudiante7.edad))+"         "+str(Estudiante7.cal1)+"     "+str(Estudiante7.cal2)+"    "+str(Estudiante7.cal3)+"     "+str(Estudiante7.cal4)+"     "+str(Estudiante7.cal5)+"    "+str(Estudiante7.final)+"     SI       "+ Estudiante72.fecha +"  "+ Estudiante72.tesis))
print ((str(Estudiante8.matricula)+ "      " + (Estudiante8.nombre)+"    "+ str((Estudiante8.edad))+"         "+str(Estudiante8.cal1)+"     "+str(Estudiante8.cal2)+"     "+str(Estudiante8.cal3)+"     "+str(Estudiante8.cal4)+"    "+str(Estudiante8.cal5)+"    "+str(Estudiante8.final)+"     SI       "+ Estudiante82.fecha +"  "+ Estudiante82.tesis))


print("")
print ("\033[46mDatos estudiantes de actuaría UTECA\033[0m")
print(Estudiante1)
print(Estudiante2)
print(Estudiante3)
print(Estudiante4)
print(Estudiante5)
print(Estudiante6)
print(Estudiante7)
print(Estudiante8)