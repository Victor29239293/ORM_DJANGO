from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Periodo
class ActivePeriodManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Period(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField() 
    end_date = models.DateField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return f"{self.start_date} - {self.end_date}"
    
    class Meta:
        verbose_name = 'period'
        verbose_name_plural = 'periods'
        ordering = ['start_date']
        indexes = [models.Index(fields=['start_date', 'end_date']),]
        
        
# Asignaturas
class ActiveSubjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]
    
# Profesores
class ActiveTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]
    
    dni = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return f"{self.name}  {self.last_name}"
    
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ['name','last_name']
        indexes = [models.Index(fields=['name','last_name']),]

    
# Estudiantes
class ActiveStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    ]
    dni = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200, )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    class Meta: 
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['name','last_name']
        indexes = [models.Index(fields=['name','last_name']),]
        

# Notas
class ActiveNoteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return f"Nota: {self.id} - Periodo: {self.period} - Profesor: {self.teacher} - Asignatura: {self.subject}"
    

# Detalle de Notas
class ActiveDetailNoteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)
    
class DetailNote(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    note1 = models.DecimalField(max_digits=5, decimal_places=2)
    note2 = models.DecimalField(max_digits=5, decimal_places=2)
    recuperation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    note_final = models.DecimalField(max_digits=5, decimal_places=2)
    observation = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)
    
    def __str__(self):
        return f"Detalle Nota: {self.id} - Estudiante: {self.student}"
    
    class Meta:
        verbose_name = 'detail note'
        verbose_name_plural = 'detail notes'
        ordering = ['note']
        indexes = [models.Index(fields=['note']),]
