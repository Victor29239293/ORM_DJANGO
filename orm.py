from datetime import date,datetime
import os
import django
from django.contrib.auth.models import User
from core.models import Period, Subject, Teacher, Student, Note, DetailNote
import random
from decimal import Decimal
from django.utils.dateparse import parse_date
from django.db.models import Sum, Avg, Max, Min, Count, F, Q, ExpressionWrapper, FloatField
from django.db.models.functions import Length


# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_academica.settings')
# Inicializa Django
django.setup()

def probar_orm():
    def create_user(create=False):
        if create:  
            User.objects.create_user(
                username='admin',
                password='12345678',
                email='admin@unemi.edu.ec'
            )
        users = User.objects.all()  

        print("Listado de Usuarios")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}")

    

    def create_periodo(create=False):
        if create:
            user = User.objects.get(username='admin')
            Period.objects.bulk_create([
                Period(start_date=date(2020, 1, 1), end_date=date(2020, 6, 30), user=user),
                Period(start_date=date(2020, 7, 1), end_date=date(2020, 12, 31), user=user),
                Period(start_date=date(2021, 1, 1), end_date=date(2021, 6, 30), user=user),
                Period(start_date=date(2021, 7, 1), end_date=date(2021, 12, 31), user=user),
                Period(start_date=date(2022, 1, 1), end_date=date(2022, 6, 30), user=user),
                Period(start_date=date(2022, 7, 1), end_date=date(2022, 12, 31), user=user),
                Period(start_date=date(2023, 1, 1), end_date=date(2023, 6, 30), user=user),
                Period(start_date=date(2023, 7, 1), end_date=date(2023, 12, 31), user=user),
                Period(start_date=date(2024, 1, 1), end_date=date(2024, 6, 30), user=user),
                Period(start_date=date(2024, 7, 1), end_date=date(2024, 12, 31), user=user),
            ])
        print('Lista de Periodos:')
        periodos = Period.objects.all()
        for periodo in periodos:
            print(f"ID: {periodo.id}, Inicio: {periodo.start_date}, Fin: {periodo.end_date}, Usuario: {periodo.user}")

   

    def create_asignatura(create=False):
        if create:
            user = User.objects.get(username='admin')
            Subject.objects.bulk_create([
                Subject(description="Programacion Orientada a Objetos", user=user),
                Subject(description="Base de Datos", user=user),
                Subject(description="Sistemas Operativos", user=user),
                Subject(description="Arquitectura de Software", user=user),
                Subject(description="Cálculo", user=user),
                Subject(description="Redes de Datos", user=user),
                Subject(description="Administración de Bases de Datos", user=user),
                Subject(description="Ecuaciones Diferenciales", user=user),
                Subject(description="Modelamiento de Software", user=user),
                Subject(description="Matemática Discreta", user=user),
            ])
        
        print('Lista de Asignaturas:')
        subjects = Subject.objects.all()
        for subject in subjects:
            print(f"ID: {subject.id}, Nombre: {subject.description}, Usuario: {subject.user}")

    

    def create_profesor(create=False):
        if create:
            user = User.objects.get(username='admin')
            Teacher.objects.bulk_create([
                Teacher(dni='0942445743', name="Juan", last_name="Perez", gender='M', user=user),
                Teacher(dni='0980800924', name="Pedro", last_name="Perez", gender='M', user=user),
                Teacher(dni='0979815253', name="Maria", last_name="Perez", gender='F', user=user),
                Teacher(dni='0924181027', name="Carlos", last_name="Gonzalez", gender='M', user=user),
                Teacher(dni='0919565218', name="Laura", last_name="Gomez", gender='F', user=user),
                Teacher(dni='0942195991', name="Miguel", last_name="Hernandez", gender='M', user=user),
                Teacher(dni='0993474287', name="Ana", last_name="Martinez", gender='F', user=user),
                Teacher(dni='0980798152', name="Luis", last_name="Lopez", gender='M', user=user),
                Teacher(dni='0978451423', name="Lucia", last_name="Sanchez", gender='F', user=user),
                Teacher(dni='0605245757', name="Diego", last_name="Ramirez", gender='M', user=user),
            ])
        
        print('Lista de Profesores:')
        teachers = Teacher.objects.all()
        for teacher in teachers:
            print(f"ID: {teacher.dni}, Nombre: {teacher.name} {teacher.last_name}, Género: {teacher.gender}, Usuario: {teacher.user}")

   

    def create_estudiante(create=False):
        if create:
            user = User.objects.get(username='admin')
            Student.objects.bulk_create([
                Student(dni='0942445743', name="Victor", last_name="Celi", gender='M', user=user),
                Student(dni='0980800924', name="David", last_name="Ruiz", gender='M', user=user),
                Student(dni='0979811234', name="Valeria", last_name="Barrera", gender='F', user=user),
                Student(dni='0941234567', name="Michelle", last_name="Barrera", gender='F', user=user),
                Student(dni='0987654321', name="Anthony", last_name="Velastegui", gender='M', user=user),
                Student(dni='0971122334', name="Sofia", last_name="Cabrera", gender='F', user=user),
                Student(dni='0969988776', name="Daniela", last_name="Cabrera", gender='F', user=user),
                Student(dni='0955544332', name="Wilmer", last_name="Cabrera", gender='M', user=user),
                Student(dni='0944433221', name="Jessica", last_name="Rivadeneira", gender='F', user=user),
                Student(dni='0987766554', name="Andres", last_name="Ruiz", gender='M', user=user),
            ])
        
        print('Lista de Estudiantes:')
        estudiantes = Student.objects.all()
        for estudiante in estudiantes:
            print(f"ID: {estudiante.dni}, Nombre: {estudiante.name} {estudiante.last_name}, Género: {estudiante.gender}, Usuario: {estudiante.user}")

    

    def create_note(create=False):
        if create:
            user = User.objects.get(username='admin')
            
            period1 = Period.objects.get(start_date='2020-01-01', end_date='2020-06-30')
            period2 = Period.objects.get(start_date='2023-01-01', end_date='2023-06-30')
            
            teacher1 = Teacher.objects.get(name='Ana', last_name='Martinez')
            teacher2 = Teacher.objects.get(name='Carlos', last_name='Gonzalez')
            teacher3 = Teacher.objects.get(name='Diego', last_name='Ramirez')
            teacher4 = Teacher.objects.get(name='Juan', last_name='Perez')
            teacher5 = Teacher.objects.get(name='Laura', last_name='Gomez')
            teacher6 = Teacher.objects.get(name='Lucia', last_name='Sanchez')
            teacher7 = Teacher.objects.get(name='Luis', last_name='Lopez')
            teacher8 = Teacher.objects.get(name='Maria', last_name='Perez')
            teacher9 = Teacher.objects.get(name='Miguel', last_name='Hernandez')
            teacher10 = Teacher.objects.get(name='Pedro', last_name='Perez')
            subject1 = Subject.objects.get(description='Administración de Bases de Datos')
            subject2 = Subject.objects.get(description='Arquitectura de Software')
            subject3 = Subject.objects.get(description='Base de Datos')
            subject4 = Subject.objects.get(description='Cálculo')
            subject5 = Subject.objects.get(description='Ecuaciones Diferenciales')
            subject6 = Subject.objects.get(description='Matemática Discreta')
            subject7 = Subject.objects.get(description='Modelamiento de Software')
            subject8 = Subject.objects.get(description='Programacion Orientada a Objetos')
            subject9 = Subject.objects.get(description='Redes de Datos')
            subject10 = Subject.objects.get(description='Sistemas Operativos')

            Note.objects.create(period=period1, teacher=teacher1, subject=subject1, user=user)
            Note.objects.create(period=period1, teacher=teacher2, subject=subject2, user=user)
            Note.objects.create(period=period1, teacher=teacher3, subject=subject3, user=user)
            Note.objects.create(period=period1, teacher=teacher4, subject=subject4, user=user)
            Note.objects.create(period=period1, teacher=teacher5, subject=subject5, user=user)
            Note.objects.create(period=period2, teacher=teacher6, subject=subject6, user=user)
            Note.objects.create(period=period2, teacher=teacher7, subject=subject7, user=user)
            Note.objects.create(period=period2, teacher=teacher8, subject=subject8, user=user)
            Note.objects.create(period=period2, teacher=teacher9, subject=subject9, user=user)
            Note.objects.create(period=period2, teacher=teacher10, subject=subject10, user=user)
        
        print("Lista de Notas")
        notas = Note.objects.all()
        for nota in notas:
            print(f"ID: {nota.id}, Periodo: {nota.period.start_date} - {nota.period.end_date}, Profesor: {nota.teacher.name} {nota.teacher.last_name}, Asignatura: {nota.subject.description}, Usuario: {nota.user.username}")

   
    
    def create_detail_nota(create=False):
        if create:
            user = User.objects.get(username='admin')
            student_dnis = [
                '0987766554', '0987654321', '0980800924', '0979811234',
                '0971122334', '0969988776', '0955544332', '0944433221',
                '0942445743', '0941234567'
            ]
            
            students = [Student.objects.get(dni=dni) for dni in student_dnis]
            note_ids = list(range(1, 11))
            notes = [Note.objects.get(id=note_id) for note_id in note_ids]
            
            for student, note in zip(students, notes):
                nota1 = random.uniform(1, 50)
                nota2 = random.uniform(1, 50)
                nota_finals = nota1 + nota2 
                recuperacion = 0 if nota_finals >= 70 else random.uniform(1, 50)
                finals = nota_finals if recuperacion == 0 and nota_finals >= 70 else (recuperacion + nota_finals) /2
                
                
                DetailNote.objects.create(
                    student=student,
                    note=note,
                    note1=nota1,
                    note2=nota2,
                    recuperation=recuperacion,
                    note_final=finals,
                    observation='Ninguna',
                    user=user
                )
            print("Detalles de notas creados exitosamente.")           
   

    #Consultar basicas:
    #EJERCICIO 1 - 16: -DAMIAN GABRIEL ORDOÑEZ OCHOA
    def filter_Estudiante(): # Ejercicio 1
            estudiante_filter = Student.objects.filter(name__istartswith='Est')
            if estudiante_filter.exists():
                print('Lista de estudiantes')
                for i in estudiante_filter:
                    print(i.name, i.last_name)
            else:
                print('No hay estudiantes con ese nombre :(')
    
        
    def filter_Profesor(): # Ejercicio 2
        profesor_filter = Teacher.objects.filter(name__icontains='or')
        if profesor_filter.exists():
            print('Lista de profesor')
            for i in profesor_filter:
                print(i.name, i.last_name)
        else:
            print('No hay profesor con ese nombre :(')
    
        
    def filter_Asignatura(): # Ejercicio 3 
        asignatura_filter = Subject.objects.filter(description__iendswith='10')
        if asignatura_filter.exists():
            print('Lista de asignaturas')
            for i in asignatura_filter:
                print(i.description)
        else:
            print('No existe asignaturas que termine en 10 ') 
        
    
        
    def nota1_filter(): # Ejercicio 4
        nota1_filter = DetailNote.objects.filter(note1__gt=8.0)
        if nota1_filter.exists():
            print('Lista de notas ')
            for i in nota1_filter:
                print(f'Estudiante: {i.student} Notas 1 : {i.note1}')
        else:
            print('No hay Notas 1')
    
        
    def nota2_filter():   # Ejercicio 5
        nota2_filter = DetailNote.objects.filter(note2__lt=9.0)
        if nota2_filter.exists():
            print('Lista de notas ')
            for i in nota2_filter:
                print(f'Estudiante: {i.student} Notas 2 : {i.note2}')
        else:
            print('No hay Notas 2')
        
  
        
    def recuperacion_filter(): # Ejercicio 6
        recuperacion_filter = DetailNote.objects.filter(recuperation=9.5)
        if recuperacion_filter.exists():
            print('Lista de notas De Recuperacion ')
            for i in recuperacion_filter:
                print(f'Estudiante: {i.student} Notas Recuperacion : {i.recuperation}')
        else:
            print('No hay Notas Recuperacion')
        
   
    #Consultas usando condiciones lógicas (AND, OR, NOT)
    def estudiante_logic(): # Ejercicio 7
        estudiante_logic = Student.objects.filter(Q(name__istartswith='v') | Q(dni__iendswith='1'))
        if estudiante_logic.exists():
            print('Lista de estudiantes')
            for i in estudiante_logic:
                print(i.name, i.dni)
        else:
            print('No hay estudiantes con ese nombre :(')
    
    
#8. Seleccionar todas las asignaturas cuya descripción contiene 'Asig' o termina en '5':
    def asignatura_logic(): # Ejercicio 8
        asignatura_logic = Subject.objects.filter(Q(description__icontains='Asig') | Q(description__iendswith='5'))
        if asignatura_logic.exists():
            print('Lista de asignaturas')
            for i in asignatura_logic:
                print(i.description)
        else:
            print('No hay asignaturas con ese nombre :(')
        
   

#9. Seleccionar todos los profesores cuyo nombre no contiene 'or':
    def profesor_logic(): # Ejercicio 9
        profesor_logic = Teacher.objects.filter(~Q(name__icontains='or'))
        if profesor_logic.exists():
            print('Lista de profesor')
            for i in profesor_logic:
                print(i.name, i.last_name)
        else:
            print('No hay profesor con ese nombre :(')
   

#10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0:
    def nota_logic(): # Ejercicio 10
        nota_logic = DetailNote.objects.filter(Q(note1__gt=7.0) & Q(note2__lt=8.0)) # > <
        print(nota_logic) 
    

#11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0:
    def recup_logic(): # Ejercicio 11
        recup_logic = DetailNote.objects.filter(Q(recuperation = None) | Q(note2__gt=100))
       
        if recup_logic.exists():
            print('Lista de notas ')
            for i in recup_logic:
                print(f'Estudiante: {i.student} Notas Recuperacion : {i.recuperation} nota2 {i.note2}')
        else:
            print('No hay Notas Recuperacion')
    
    
# Consulta utilizando funciones numericas
#12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0:
    def rango_nota1(): # Ejercicio 12
        nota1_rango = DetailNote.objects.filter(note1__range=(7.0,9.0))
        if nota1_rango.exists():
            print('Lista de notas ')
            for i in nota1_rango:
                print(f'Estudiante: {i.student} Notas 1 : {i.note1}')
        else:
            print('No hay Notas 1')
    

#13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0:

    def rango_nota2(): # Ejercicio 13
        nota2_rango= DetailNote.objects.exclude(note2__range=(6.0,8.0))
        if nota2_rango.exists():
            print('Lista de notas ')
            for i in nota2_rango:
                print(f'Estudiante: {i.student} Notas 2 : {i.note2}')
        else:
            print('No hay Notas 2 con ese rango')
   

#14. todas las notas cuya recuperacion no sea None:
    def none_recuperacion(): # Ejercicio 14
        recuperacion_rango= DetailNote.objects.exclude(recuperation=None)
        if recuperacion_rango.exists():
            print('Lista de notas ')
            for i in recuperacion_rango:
                print(f'Estudiante: {i.student} Notas Recuperacion : {i.recuperation}')
        else:
            print('No hay Notas Recuperacion')
    
# Consultas usando funciones de fecha (asumiendo que los modelos incluyen campos de fecha)
#15. Seleccionar todas las notas creadas en el último año:
    def notas_ultimo_year():    # ejercicio 15
        notas = Note.objects.filter(created__year=datetime.now().year)
        if notas.exists():
            print('Lista de notas ')
            for i in notas:
                print(f'Fecha Creada {i.created} Materias {i.subject}')
        else:
            print('No hay Notas Creada el Ultimo Año')
   
    
#16. Seleccionar todas las notas creadas en el último mes:
    def notas_creadas_mes():    # ejercicio 16
        notas = Note.objects.filter(created__month=datetime.now().month)
        if notas.exists():
            print('Lista de notas ')
            for i in notas:
                print(f'Fecha Creada {i.created} Materias {i.subject}')
        else:
            print('No hay Notas Creada el Ultimo Mes')
    
    
#17. Seleccionar todas las notas creadas en el último día:
    def notas_cread_day():
        notas = Note.objects.filter(created__day=datetime.now().day)
        if notas.exists():
            print('Lista de notas ')
            for i in notas:
                print(f'Fecha Creada {i.created} Materias {i.subject}')
        else:
            print('No hay Notas Creada el Ultimo Día')
    

#18. Seleccionar todas las notas creadas antes del año 2023:
    def notas_cread_year():
        notas = Note.objects.filter(created__year__lt=2023)
        if notas.exists():
            print('Lista de notas ')
            for i in notas:
                print(f'Fecha Creada {i.created} Materias {i.subject}')
        else:
            print('No hay Notas Creada antes del Año 2023')
    
    
#19. Seleccionar todas las notas creadas en marzo de cualquier año:
    def notas_cread_year():
        notas = Note.objects.filter(created__month=3)
        if notas.exists():
            print('Lista de notas ')
            for i in notas:
                print(f'Fecha Creada {i.created} Materias {i.subject}')
        else:
            print('No hay Notas Creada en Marzo')
    

# Consultas combinadas con funciones avanzadas
    # 20. Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10
    # caracteres:
    def student_name():
        student = Student.objects.annotate(name_length=Length('name')).filter(name_length=10)
        if student.exists():
            print('Lista de estudiantes con nombres de 10 caracteres:')
            for s in student:
                print(f'Nombre: {s.name}')
        else:
            print('No hay estudiantes con nombres de exactamente 10 caracteres.')
    
    
#21. Seleccionar todas las notas con nota1 y nota2 mayores a 7.5:
    def nota1_nota2():
        nota1_nota2 = DetailNote.objects.filter(note1__gt=7.5, note2__gt=7.5)
        if nota1_nota2.exists():
            print('Lista de notas ')
            for i in nota1_nota2:
                print(f'Estudiante: {i.student} Notas 1 : {i.note1} Notas 2 : {i.note2}')
        else:
            print('No existe notas mayores a 7.5')
    
    
#22. Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2:
    def notas_recuperacion():
        # Seleccionar todas las notas con recuperación no nula y nota1 mayor a nota2
        notas = DetailNote.objects.filter(recuperation__isnull=False, note1__gt=F('note2'))

        # Validar si se encontraron notas
        if notas.exists():
            print('Lista de notas:')
            for nota in notas:
                print(f'Estudiante: {nota.student}, Nota1: {nota.note1}, Nota2: {nota.note2}, Recuperación: {nota.recuperation}')
        else:
            print('No hay notas con recuperación no nula y nota1 mayor que nota2.')

    
#23. Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5:
    def nota1_nota2():
        nota1_nota2 = DetailNote.objects.filter(note1__gt=8.0) | DetailNote.objects.filter(note2=7.5)
        if nota1_nota2.exists():
            print('Lista de notas')
            for i in nota1_nota2:
                print(f'Estudiante: {i.student} Nota 1: {i.note1} Nota 2: {i.note2}')
        else:
            print('No existen notas con nota1 mayor a 8.0 o nota2 igual a 7.5')

    

#24. Seleccionar todas las notas con recuperacion mayor a nota1 y nota2:

    def recuperation_mayor():
        notas = DetailNote.objects.filter(Q(recuperation__gt=F('note1')) & Q(recuperation__gt=F('note2')))
        if notas.exists():
            print('Lista de notas')
            for nota in notas:
                print(f'Estudiante: {nota.student}, Nota 1: {nota.note1}, Nota 2: {nota.note2}, Recuperación: {nota.recuperation}')
        else:
            print('No existen notas con recuperación mayor a nota1 y nota2.')

    

#Consultas con subconsultas y anotaciones
#25. Seleccionar todos los estudiantes con al menos una nota de recuperación:
    def students_with_recuperation():
        student_name = Student.objects.filter(detailnote__recuperation__isnull=False).distinct()
        if student_name.exists():
            print('Lista de estudiantes con al menos una nota de recuperación:')
            for student in student_name:
                print(f'Nombre: {student.name}')
        else:
            print('No hay estudiantes con notas de recuperación.')

   
#26. Seleccionar todos los profesores que han dado una asignatura específica:

    def professors_teaching_subject(subject_id):
        professors = Teacher.objects.filter(note__subject_id__description=subject_id).distinct()
        
        if professors.exists():
            print('Lista de profesores que han dado la asignatura específica:')
            for professor in professors:
                print(f'Nombre: {professor.name}')
        else:
            print('No hay profesores que hayan dado la asignatura específica.')

   
    
#27. Seleccionar todas las asignaturas que tienen al menos una nota registrada:
    def subjects_with_notes():
        subjects = Subject.objects.filter(note__isnull=False).distinct()
        
        if subjects.exists():
            print('Lista de asignaturas con al menos una nota registrada:')
            for subject in subjects:
                print(f'Asignatura: {subject.description}')
        else:
            print('No hay asignaturas con notas registradas.')

    
    
#28. Seleccionar todas las asignaturas que no tienen notas registradas:
    def subjects_without_notes():
        subjects = Subject.objects.filter(note__isnull=True).distinct()
        
        if subjects.exists():
            print('Lista de asignaturas sin notas registradas:')
            for subject in subjects:
                print(f'Asignatura: {subject.description}')
        else:
            print('No hay asignaturas sin notas registradas.')

    
    
#29. Seleccionar todos los estudiantes que no tienen notas de recuperación:
    def students_without_recuperation():
        students = Student.objects.exclude(detailnote__recuperation__isnull=False).distinct()
        
        if students.exists():
            print('Lista de estudiantes sin notas de recuperación:')
            for student in students:
                print(f'Nombre: {student.name}')
        else:
            print('No hay estudiantes sin notas de recuperación.')

   

#30. Seleccionar todas las notas cuyo promedio de nota1 y nota2 es mayor a 8.0:
    def notes_with_avg_above_8():
        avg_expression = ExpressionWrapper((F('note1') + F('note2')) / 2.0, output_field=FloatField())
        notes = DetailNote.objects.annotate(avg=avg_expression).filter(avg__gt=8.0)
        
        if notes.exists():
            print('Lista de notas con promedio de nota1 y nota2 mayor a 8.0:')
            for note in notes:
                print(f'Estudiante: {note.student.name}, Nota 1: {note.note1}, Nota 2: {note.note2}, Promedio: {note.avg}')
        else:
            print('No existen notas con promedio de nota1 y nota2 mayor a 8.0.')


#31. Seleccionar todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0:
    def notes_with_specific_conditions():
        notes = DetailNote.objects.filter(note1__lt=6.0, note2__gt=7.0)
        
        if notes.exists():
            print('Lista de notas con nota1 menor que 6.0 y nota2 mayor que 7.0:')
            for note in notes:
                print(f'Estudiante: {note.student.name}, Nota 1: {note.note1}, Nota 2: {note.note2}')
        else:
            print('No existen notas con nota1 menor que 6.0 y nota2 mayor que 7.0.')

   

#32. Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:
    def notes_with_note1_in_list():
        notes = DetailNote.objects.filter(note1__in=[7.0, 8.0, 9.0])
        
        if notes.exists():
            print('Lista de notas con nota1 en [7.0, 8.0, 9.0]:')
            for note in notes:
                print(f'Estudiante: {note.student.name}, Nota 1: {note.note1}, Nota 2: {note.note2}')
        else:
            print('No existen notas con nota1 en [7.0, 8.0, 9.0].')

    
#33. Seleccionar todas las notas cuyo id está en un rango del 1 al 5:
    def notes_with_id_in_range():
        notes = DetailNote.objects.filter(id__range=(1, 5))
        
        if notes.exists():
            print('Lista de notas con id en el rango del 1 al 5:')
            for note in notes:
                print(f'Estudiante: {note.student.name}, Nota 1: {note.note1}, Nota 2: {note.note2}, ID: {note.id}')
        else:
            print('No existen notas con id en el rango del 1 al 5.')

   
    
     # 34. Seleccionar todas las notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:
    def select_grades_not_in_list():
        grades = DetailNote.objects.exclude(recuperation__in=[8.0, 9.0, 10.0])
        for grade in grades:
            print(f"ID: {grade.id}, Recuperation: {grade.recuperation}")
    
    # 35. Suma de todas las notas de un estudiante:
    def sum_all_grades_of_student(student_id):
        total = DetailNote.objects.filter(student_id=student_id).aggregate(total_grades=Sum('note_final'))

        total_grades = total['total_grades'] if total['total_grades'] is not None else 0.0

        print(f"Total grades for student {student_id}: {round(total_grades, 2)}")

    # 36. Nota máxima obtenida por un estudiante:
    def max_grade_of_student(student_id):
        max_grade = DetailNote.objects.filter(student__dni=student_id).aggregate(max_grade=Max('note_final', 'note1', 'note2'))
        print(f"Maximum grade for student {student_id}: {max_grade['max_grade']}")

    # 37. Nota mínima obtenida por un estudiante:
    def min_grade_of_student(student_id):
        min_grade = DetailNote.objects.filter(student__dni=student_id).aggregate(min_grade=Min('note_final', 'note1', 'note2'))
        print(f"Minimum grade for student {student_id}: {min_grade['min_grade']}")

    # 38. Contar el número total de notas de un estudiante:
    def count_grades_of_student(student_id):
        total_grades = DetailNote.objects.filter(student__dni=student_id).count()
        print(f"Total number of grades for student {student_id}: {total_grades}")
    
    # 39. Promedio de todas las notas de un estudiante sin incluir recuperación
    def average_grades_excluding_recuperation(student_id):
        average = DetailNote.objects.filter(student__dni=student_id).exclude(recuperation__isnull=False).aggregate(avg_grade=Avg('note_final'))
        print(f"Average grade for student {student_id}, excluding recuperation: {average['avg_grade']}")
    
    # CONSULTAS CON SUBCONSULTAS CON LOS MODELOS RELACIONADO. APLICAR RELACIONES INVERSAS DONDE SEA NECESARIO
    
    # 40. Dado un estudiante obtener todas sus notas con el detalle de todos sus datos relacionados:
    def get_student_grades_details(student_id):
        details = DetailNote.objects.filter(student__dni=student_id).select_related('note', 'note__period', 'note__teacher', 'note__subject')
        for detail in details:
            print(f"Grade ID: {detail.id}, Student: {detail.student}, Period: {detail.note.period}, Teacher: {detail.note.teacher}, Subject: {detail.note.subject}")

    # 41. Obtener todas las notas de un período específico:
    def get_grades_for_period(period_id):
        grades = DetailNote.objects.filter(note__period__id=period_id)
        for grade in grades:
            print(f"Grade ID: {grade.id}, Period: {grade.note.period}, Grade: {grade.note_final}")

    # 42. Consultar todas las notas de una asignatura dada en un período:
    def get_grades_for_subject_in_period(subject_id, period_id):
        grades = DetailNote.objects.filter(note__subject__id=subject_id, note__period__id=period_id)
        for grade in grades:
            print(f"Grade ID: {grade.id}, Subject: {grade.note.subject}, Period: {grade.note.period}, Grade: {grade.note_final}")

    # 43. Obtener todas las notas de un profesor en particular:
    def get_grades_for_teacher(teacher_id):
        grades = DetailNote.objects.filter(note__teacher__dni=teacher_id)
        for grade in grades:
            print(f"Grade ID: {grade.id}, Teacher: {grade.note.teacher}, Grade: {grade.note_final}")

    # 44. Consultar todas las notas de un estudiante con notas superiores a un valor dado:
    def get_grades_above_value(student_id, value):
        grades = DetailNote.objects.filter(student__dni=student_id, note_final__gt=value)
        for grade in grades:
            print(f"Grade ID: {grade.id}, Student: {grade.student}, Grade: {grade.note_final}")

    # 45. Obtener todas las notas de un estudiante ordenadas por período:
    def get_grades_ordered_by_period(student_id):
        grades = DetailNote.objects.filter(student__dni=student_id).order_by('note__period__start_date')
        for grade in grades:
            print(f"Grade ID: {grade.id}, Student: {grade.student}, Period: {grade.note.period}, Grade: {grade.note_final}")

    # 46. Consultar la cantidad total de notas para un estudiante:
    def total_grades_for_student(student_id):
        total_grades = DetailNote.objects.filter(student__dni=student_id).count()
        print(f"Total grades for student {student_id}: {total_grades}")

    # 47. Calcular el promedio de las notas de un estudiante en un período dado:
    def average_grade_in_period(student_id, period_id):
        average = DetailNote.objects.filter(student__dni=student_id, note__period__id=period_id).aggregate(avg_grade=Avg('note_final'))
        print(f"Average grade for student {student_id} in period {period_id}: {average['avg_grade']}")

    # 48. Consultar todas las notas con una observación específica:
    def get_grades_with_observation(observation):
        grades = DetailNote.objects.filter(observation=observation)
        for grade in grades:
            print(f"Grade ID: {grade.id}, Observation: {grade.observation}, Grade: {grade.note_final}")
#49. Obtener todas las notas de un estudiante ordenadas por asignatura:   
    def get_note_subject(student_cedula):
        detail_notes = DetailNote.objects.filter(student__dni=student_cedula).order_by('note__subject__description')
        for detail_note in detail_notes:
            student= detail_note.student.name
            last_name= detail_note.student.last_name
            asignatura = detail_note.note.subject.description
            nota1 = detail_note.note1
            nota2 = detail_note.note2
            recuperacion = detail_note.recuperation
            nota_final = detail_note.note_final
            print('--------------------------------------------------------')
            print('Notas del Estudiante por asignatura:')
            print('--------------------------------------------------------')
            print(f'Estudiante: {student} {last_name}')
            print('--------------------------------------------------------')
            print(f" Asignatura: {asignatura}")
            print('--------------------------------------------------------')
            print(f'  Nota1: {nota1} \n  Nota2: {nota2},\n  Recuperación: {recuperacion},\n  final note: {nota_final}')
   
    
#Sentencias Update:
#50. Actualizar nota1 para alumnos con nota1 < 20:
    def update_note1():
       
        detail_note = DetailNote.objects.filter(note1__lte=20)
        for note in detail_note:
            note.note1 = random.uniform(1, 50)
            note.save()
        print("Notas actualizadas correctamente.")
    

#51. Actualizar nota2 para alumnos con nota2 < 15:
    def update_note2():
        detail_note = DetailNote.objects.filter(note2__lte=15)
        for note in detail_note:
            note.note2 = random.uniform(1, 50)
            note.save()
            print("Notas actualizadas correctamente.")
    

#52. Actualizar recuperación para alumnos con recuperación < 10:
    def update_note_recuperation():
        detail_note = DetailNote.objects.filter(recuperation__lt = 10)
        for note in detail_note:
            note.recuperation = random.uniform(1,100)
            note.save()
        print("Notas actualizadas correctamente.")
    
    
#53. Actualizar observación para alumnos que hayan aprobado:
    def update_observation():
        detail_note = DetailNote.objects.filter(note_final__gte = 70)
        for observation in detail_note:
            observation.observation = 'Aprobado'
            observation.save()
        print("Observaciones actualizadas correctamente.")
    
    
    
#54. Actualizar todas las notas en un período específico:
    def update_periodo_note(start_date_str, end_date_str):
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        if not start_date or not end_date:
            print("Fechas inválidas. Asegúrate de que las fechas estén en el formato correcto.")
            return

        detail_notes = DetailNote.objects.filter(
            note__period__start_date__lte=end_date,
            note__period__end_date__gte=start_date
        )
        for detail_note in detail_notes:
            print(f"Antes de la actualización: ID {detail_note.id}, note1: {detail_note.note1}")

            detail_notes.update(note1=random.uniform(1,100))  

            updated_notes = DetailNote.objects.filter(
                note__period__start_date__lte=end_date,
                note__period__end_date__gte=start_date
            )
            for detail_note in updated_notes:
                print(f"Después de la actualización: ID {detail_note.id}, note1: {detail_note.note1}")

            print("Notas actualizadas correctamente.")
            
#Sentencias delete
#55. Eliminar físicamente todas las notas de un estudiante:
    def delete_student_notes(student_id):
        detail_notes = DetailNote.objects.filter(student__dni=student_id)
        for detail_note in detail_notes:
            detail_note.delete()
        print("Notas eliminadas correctamente.")
    
#56. Eliminar lógicamente todas las notas de un estudiante (en el campo state
#que indica si el registro está activo o no):

    def logical_delete_student_notes(student_id):
  
        detail_notes = DetailNote.objects.filter(student__dni=student_id)
        if detail_notes.exists():
            detail_notes.update(state=False) 
            print("Notas eliminadas lógicamente correctamente.")
        else:
            print("No se encontraron notas para el estudiante con ID:", student_id)

    

#57. Eliminar físicamente todas las notas de un período específico:
    def delete_notes_by_period(period_id):
         # Filtrar las notas que pertenecen al período especificado
        notas = Note.objects.filter(period_id=period_id)

        # Filtrar las DetalleNota que pertenecen a esas notas
        detalle_notas = DetailNote.objects.filter(note__in=notas)

        # Verificar si existen DetalleNota para eliminar
        if detalle_notas.exists():
            detalle_notas.delete()
            print("Notas eliminadas correctamente para el período:", period_id)
        else:
            print("No se encontraron notas para el período:", period_id)
    
    
#58. Eliminar lógicamente todas las notas de un período específico:
    def logical_delete_notes_by_period(start_date, end_date):
        try:
            # Filtrar el período especificado
            period = Period.objects.get(start_date=start_date, end_date=end_date)
            
            # Filtrar las notas que pertenecen al período especificado
            notes = Note.objects.filter(period=period)
            
            # Filtrar las notas de detalle asociadas a las notas encontradas
            detail_notes = DetailNote.objects.filter(note__in=notes)
            
            # Verificar si existen notas de detalle para el período especificado
            if detail_notes.exists():
                # Actualizar el campo 'state' a False para eliminar lógicamente
                detail_notes.update(state=False)
                print("Notas eliminadas lógicamente correctamente para el período:", start_date, " - ", end_date)
            else:
                print("No se encontraron notas para el período:", start_date, " - ", end_date)
        
        except Period.DoesNotExist:
            print("El período especificado no existe:", start_date, " - ", end_date)

   

   

#59. Eliminar físicamente todas las notas que tengan una nota1 menor a 10:
    def delete_notes_with_nota1_less_than_10():
    
        detail_notes = DetailNote.objects.filter(note1__lt=10)
        if detail_notes.exists():
            detail_notes.delete()
            print("Notas con nota1 menor a 10 eliminadas correctamente.")
        else:
            print("No se encontraron notas con nota1 menor a 10.")
  
   
#60. Crea un registro de notas de un estudiante, simulando una inserción de los
# datos tal como se explicó en el ejercicio de la creación de una factura con su
# detalle de productos en el archivo orm.py de la clase impartida.

    def create_student_detail_note(
    estudiante_dni, estudiante_nombre, estudiante_apellido, estudiante_genero,
    periodo_start_date, periodo_end_date,
    profesor_dni, profesor_nombre, profesor_apellido, profesor_genero,
    asignatura_descripcion,
    nota1, nota2, recuperation=None, observation=None, user=None
):
        try:
            if user is None:
                raise ValueError("El usuario no puede ser None")

            estudiante, created = Student.objects.get_or_create(
                dni=estudiante_dni,
                defaults={
                    'name': estudiante_nombre,
                    'last_name': estudiante_apellido,
                    'gender': estudiante_genero,
                    'user': user
                }
            )
            if created:
                print(f"Estudiante {estudiante_nombre} {estudiante_apellido} creado correctamente.")
            else:
                print(f"Estudiante {estudiante_nombre} {estudiante_apellido} ya existe.")

            
            periodo, created = Period.objects.get_or_create(
                start_date=periodo_start_date,
                end_date=periodo_end_date,
                defaults={'user': user}
            )
            if created:
                print(f"Periodo {periodo_start_date} - {periodo_end_date} creado correctamente.")
            else:
                print(f"Periodo {periodo_start_date} - {periodo_end_date} ya existe.")

           
            profesor, created = Teacher.objects.get_or_create(
                dni=profesor_dni,
                defaults={
                    'name': profesor_nombre,
                    'last_name': profesor_apellido,
                    'gender': profesor_genero,
                    'user': user
                }
            )
            if created:
                print(f"Profesor {profesor_nombre} {profesor_apellido} creado correctamente.")
            else:
                print(f"Profesor {profesor_nombre} {profesor_apellido} ya existe.")

            asignatura, created = Subject.objects.get_or_create(
                description=asignatura_descripcion,
                defaults={'user': user}
            )
            if created:
                print(f"Asignatura {asignatura_descripcion} creada correctamente.")
            else:
                print(f"Asignatura {asignatura_descripcion} ya existe.")

            
            nota, created = Note.objects.get_or_create(
                period=periodo,
                teacher=profesor,
                subject=asignatura,
                defaults={'user': user}
            )
            if created:
                print("Nota creada correctamente.")
            else:
                print("Nota ya existe.")

            note_final = nota1 + nota2
            applied_recuperation = 0

            if note_final < 70 and recuperation is not None:
                note_final = (note_final + recuperation) / 2
                applied_recuperation = recuperation

            detail_note = DetailNote.objects.create(
                student=estudiante,
                note=nota,
                note1=nota1,
                note2=nota2,
                recuperation=applied_recuperation,
                note_final=note_final,
                observation=observation,
                user=user
            )
            print("Detalle de nota creado correctamente:", detail_note)

        except Exception as e:
            print("Ocurrió un error al crear el detalle de nota:", str(e))

    


    
   
    create_user(True)
    create_periodo(create=True)
    create_asignatura(create=True)
    create_profesor(create=True)
    create_estudiante(create=True)
    create_note(create=True)
    create_detail_nota(create=True)
    # filter_Estudiante()
    # filter_Profesor()
    # filter_Asignatura()
    # nota1_filter()
    # nota2_filter()
    # recuperacion_filter()
    # estudiante_logic()
    # asignatura_logic()
    # profesor_logic()
    # nota_logic()
    # recup_logic()
    # rango_nota1()
    # rango_nota2() 
    # none_recuperacion() 
    # notas_ultimo_year()
    # notas_creadas_mes()
    # notas_cread_day()
    # notas_cread_year()
    # notas_cread_year()
    # student_name()
    # nota1_nota2()
    # notas_recuperacion()
    # nota1_nota2() 
    # recuperation_mayor()
    # students_with_recuperation()
    # professors_teaching_subject('Base de Datos')
    # subjects_with_notes()
    # subjects_without_notes() 
    # students_without_recuperation()
    # notes_with_avg_above_8()
    # notes_with_specific_conditions()
    # notes_with_note1_in_list()
    # notes_with_id_in_range()
    # select_grades_not_in_list()
    # sum_all_grades_of_student('0942445743')   
    # max_grade_of_student('0942445743')
    # min_grade_of_student('0942445743')
    # count_grades_of_student('0942445743')
    # average_grades_excluding_recuperation('0942445743')
    
    # get_student_grades_details('0942445743')
    # get_grades_for_period(1)
    # get_grades_for_subject_in_period(2, 1)
    # get_grades_for_teacher('0942445743')
    # get_grades_above_value('0942445743', 20)
    # get_grades_ordered_by_period('0942445743')
    # total_grades_for_student('0942445743')
    # average_grade_in_period('0942445743', 7)
    # get_grades_with_observation('Ninguna')
    # get_note_subject('0987654321')
    # update_note1()
    # update_note2()
    # update_note_recuperation()     
    # update_observation()
    # update_periodo_note('2020-01-01', '2020-06-30')
    # delete_student_notes('0942445743')
    # logical_delete_student_notes('0944433221')
    # delete_notes_by_period(1)
    # logical_delete_notes_by_period('2023-01-01', '2023-06-30')
    
    
    # delete_notes_with_nota1_less_than_10()
    # create_student_detail_note(
    #     estudiante_dni='0942445743',
    #     estudiante_nombre='Jose',
    #     estudiante_apellido='Sanchez',
    #     estudiante_genero='M',
    #     periodo_start_date='2023-01-01',
    #     periodo_end_date='2023-06-01',
    #     profesor_dni='1234567890',
    #     profesor_nombre='John',
    #     profesor_apellido='Smith',
    #     profesor_genero='M',
    #     asignatura_descripcion='Base de Datos',
    #     nota1=28,
    #     nota2=20,
    #     recuperation=100, 
    #     observation=None,
    #     user=User.objects.get(username='admin')  )



    
    
        
   
