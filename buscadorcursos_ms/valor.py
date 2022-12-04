import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","busquedorcursos.settings")

django.setup()

from Buscador.models import Campus, Faculty, Career, Place, Schedule, Types_Conditions, Subjectsconditions, Condition, Types_Typologys, Subject, Group


def ingresarcampus():
    campus = [[1101, "Bogota"],[1126,"Sede Caribe"], [1103, "Sede Mnaizales"], [1102, "Medellin"]]
    for i in campus:
        dato = Campus.objects.create(Id_campus = i[0], Name_campus = i[1])
        dato.save()
    ingresarfacultad()

        #[[2055, "Ingenierí­a de Ingenieria", [1101]],[2056,"Facultad de medicina", [1101]]]
def ingresarfacultad():
    datos = [[2055, "Ingenierí­a de Ingenieria", [1101]],[2056,"Facultad de medicina", [1101]]]
    for i in datos:
        dato = Faculty.objects.create(Id_faculty = i[0], Name_faculty = i[1])
        dato.save()
        for j in i[2]:
            dato.Id_campus.add(j)
    ingresarcarrera()
    
            
        
def ingresarcarrera():
    carrera = [[2879, "Ingenierí­a de Sistemas y Computación", 2055],[2547,"Ingeniería Mecánica", 2055]]
    for i in carrera:
        dato = Career.objects.create(Id_career = i[0], Name_career = i[1], Id_faculty = Faculty(Id_faculty = i[2]))
        dato.save()
    ingresarlugar()
        
def ingresarlugar():
    datos = [[1, 101, "Edificio de Ingenieria", 202, "Sala de sistemas"],[2,101, "Edificio de Ingenieria", 205, "Aula de clases"]]
    for i in datos:
        dato = Place.objects.create(Id_place = i[0], Place_numbertower = i[1], Place_nametower = i[2], Place_numbersalon = i[3], Place_namesalon = i[4])
        dato.save()    
    ingresarhorario()    

def ingresarhorario():
    datos = [[10709,"monday","09:00:00","07:00:00",1],
             [10911,"monday","11:00:00","09:00:00",1],
             [11113,"monday", "13:00:00","11:00:00",1],
             [11416,"monday", "16:00:00","14:00:00",2],
             [11618,"monday","18:00:00","16:00:00",1],
             [11820,"monday","20:00:00","18:00:00",1],
             [20709,"tuesday","09:00:00","07:00:00",2],
             [20911,"tuesday","11:00:00","09:00:00",1],
             [21113,"tuesday","13:00:00","11:00:00",1],
             [21416,"tuesday","16:00:00","14:00:00",2],
             [21618,"tuesday","18:00:00","16:00:00",1],
             [21820,"tuesday","20:00:00","18:00:00",2],
             [30709,"wednesday","09:00:00","07:00:00",1],
             [30911,"wednesday","11:00:00","09:00:00",1],
             [31113,"wednesday","13:00:00","11:00:00",2],
             [31416,"wednesday","16:00:00","14:00:00",1],
             [31618,"wednesday","18:00:00","16:00:00",1],
             [31820,"wednesday","20:00:00","18:00:00",1],
             [40709,"thursday","09:00:00","07:00:00",2],
             [40911,"thursday","11:00:00","09:00:00",1],
             [41113,"thursday","13:00:00","11:00:00",1],
             [41416,"thursday","16:00:00","14:00:00",2],
             [41618,"thursday","18:00:00","16:00:00",1],
             [41820,"thursday","20:00:00","18:00:00",1],
             [50709,"friday","09:00:00","07:00:00",2],
             [50911,"friday","11:00:00","09:00:00",1],
             [51113,"friday","13:00:00","11:00:00",1],
             [51416,"friday","16:00:00","14:00:00",2],
             [51618,"friday","18:00:00","16:00:00",2],
             [51820,"friday","20:00:00","18:00:00",1],
             [60709,"saturday","09:00:00","07:00:00",1],
             [60911,"saturday","11:00:00","09:00:00",1],
             [61113,"saturday","13:00:00","11:00:00",1],
             [61416,"saturday","16:00:00","14:00:00",2],
             [61618,"saturday","18:00:00","16:00:00",1],
             [61820,"saturday","20:00:00","18:00:00",2]]
    for i in datos:
        dato = Schedule.objects.create(Id_Schedule = i[0], day_name = i[1], Star_time = i[2], End_time = i[3], Id_place = Place(Id_place = i[4]))
        dato.save()
    ingresartipodecontidion()

def ingresartipodecontidion():
    datos = [["D", "no se puede matricular la asignatura sin superar el prerrequisito"],
             ["V", "podrá matricular, pero no ser calificado sin la superación del prerrequisito"],
             ["B", "matricula el prerrequisito simultáneamente, o lo ha matriculado alguna vez"],
             ["A", "anulación por incompatibilidad. Si se matricula de las dos asignaturas afectadas por el prerrequisito y no supera la asignatura llave, las asignaturas afectadas por el prerrequisito aparecerán como anuladas."]]
    for i in datos:
        dato = Types_Conditions.objects.create(Id_types = i[0], Description = i[1])
        dato.save()
    ingresarmateriadecontidion()   
        
def ingresarmateriadecontidion():
    datos = [[1000003,"Álgebra lineal"], 
             [1000004,"Cálculo diferencial"],
             [1000005,"Cálculo integral"],
             [1000006,"Cálculo en varias variables"],
             [2015215,"Análisis de sistemas variables"],
             [2015711,"Dibujo básico"],
             [2015942,"Aplicaciones de elementos finitos"],
             [2015970,"Métodos numéricos"],
             [2016353,"Bases de datos"],
             [2017257,"Dibujo de máquinas"],
             [2018009,"Psiquiatria I"],
             [2018069,"Contrapunto II"],
             [2023498,"Arte y cerebro"],
             [2025964,"Matemáticas discretas II"],
             [2025971,"Optimización"]]
    for i in datos:
        dato = Subjectsconditions.objects.create(Id_Subjectconditions = i[0], Name_subjectconditions = i[1])
        dato.save()
    ingresarcontidion()
        
def ingresarcontidion():
    datos = [#[1, 1, [2018009], "A",1,True],
             #[2, 1, [2018069], "A",1,True],
             [3, 1, [2023498], "B",1,True],
             [4, 1, [2025964], "D",1,True]]
    
    for i in datos:
        dato = Condition.objects.create(Id_condition = i[0], number_condition = i[1], Type_condition = Types_Conditions(Id_types = i[3]), Number_subject= i[4], All_subjects= i[5])
        dato.save()
        
        for j in i[2]:
            dato.Subject_condition.add(j)
    ingresartipologias()
            

def ingresartipologias():
    datos = [[1, "Fundamental Obligatoria"],
             [2, "Fundamental Optativa"],
             [3, "Disciplinar Obligatoria"],
             [4, "Disciplinar Optativa"],
             [5, "Nivelación"],
             [6, "Libre Eleccion"],
             [7, "Trabajo de grado"]]
    
    for i in datos:
        dato = Types_Typologys.objects.create(Id_typology = i[0], Name_typology = i[1])
        dato.save()
    ingresarmaterias()
        
def ingresarmaterias():
    datos = [[2017257,"Dibujo de máquinas",4,6, "asdasdasdasdasdasdasd",[2879] , [1]],
             [1000003,"Álgebra lineal",4,2, "asddasjndaddaanjjnads", [2879], [1]]]
    
    for i in datos:
        dato = Subject.objects.create(Id_subject = i[0], Name_subject = i[1], Credits= i[2], Typology=Types_Typologys(Id_typology=i[3]), Description= i[4])
        dato.save()
        
        for j in i[5]:
            dato.Id_career.add(j)
        for k in i[6]:
            dato.Id_career.add(j)
    
    ingresargrupos()
        
    
def ingresargrupos():
    datos = [[20172571, "Virtual", "Jonatan Gomez Perdomo", "2022-08-08", "2022-12-02" , "Semestral", "Diurna", 30,[2055], 2017257, [20911]],
             [10000031, "Presencial", "Jeisson Andres Vergara", "2022-08-08", "2022-12-02", "Semestral", "Diurna", 30,[2055], 1000003, [10709]]]
    
    for i in datos:
        dato = Group.objects.create( Id_group = i[0], Modality = i[1], Teacher= i[2], Date_start = i[3], Date_finish = i[4], Duration = i[5], Working_day= i[6], Slots=i[7])
        dato.save()
        for j in i[8]:
            dato.Id_faculty.add(j)
        for k in i[10]:
            dato.Id_schedule.add(k)
    return 0

def inicio():
    if __name__ == '__main__':
        print("Creando población . . Por favor espere :D")
        inicio = time.strftime("%c")
        print("Fecha y hora de inicio: "+time.strftime("%c"))
        ingresarcampus()
        fin = time.strftime("%c")
        print("Fecha y hora de inicio: "+time.strftime("%c"))
        print("Inicio: "+str(inicio)+" - Fin: "+str(fin))
        print("Población completa!! :D")
