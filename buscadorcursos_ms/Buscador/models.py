
from pyexpat import model
from django.db import models

# Create your models here.

class Campus(models.Model):
    Id_campus = models.IntegerField(primary_key=True)
    Name_campus = models.CharField(max_length=30)
    
    def __str__(self):
        return str(f"{self.Id_campus}: {self.Name_campus}")

class Faculty(models.Model):
    Id_faculty = models.IntegerField(primary_key=True)
    Name_faculty = models.CharField(max_length=100)
    Id_campus = models.ManyToManyField(Campus, related_name="Facultys", blank=True)
    
    def __str__(self):
        return '%d: %s' % (self.Id_faculty, self.Name_faculty)

class Career(models.Model):
    Id_career = models.IntegerField(primary_key=True)
    Name_career = models.CharField(max_length=100)
    Id_faculty = models.ForeignKey(Faculty, null = True, related_name="Careers", blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f"{self.Id_career}: {self.Name_career}")
    
class Place(models.Model):
    Id_place = models.IntegerField(primary_key=True)
    Place_numbertower = models.IntegerField()
    Place_nametower = models.CharField(max_length=200)
    Place_numbersalon = models.IntegerField()
    Place_namesalon = models.CharField(max_length=200)
    
    
    def __str__(self):
        return str('Lugar %d: %d-%d. %s - %s.' % (self.Id_place, self.Place_numbertower, self.Place_numbersalon, self.Place_nametower, self.Place_namesalon))

class Schedule(models.Model):
    Id_Schedule = models.IntegerField(primary_key=True)
    day_name = models.CharField(max_length=30, default="Sin dia")
    Star_time = models.TimeField(null=True, blank=True)
    End_time = models.TimeField(null=True, blank=True)
    Id_place = models.ForeignKey(Place, null = True,blank = True, on_delete=models.CASCADE)
    
    
    def __str__(self):

        return str(f'Horario {self.Id_Schedule}: dia {self.day_name} con horario de {self.Star_time} - {self.End_time}')
    
class Types_Conditions(models.Model):
    Id_types = models.CharField(max_length=5, primary_key=True)
    Description = models.TextField()
    
    def __str__(self):
        return self.Id_types
    
class Subjectsconditions(models.Model):
    Id_Subjectconditions =  models.IntegerField(primary_key=True)
    Name_subjectconditions = models.CharField(max_length=100)
    def __str__(self):
        return '(%d) %s' % (self.Id_Subjectconditions, self.Name_subjectconditions)
    
class Condition(models.Model):
    Id_condition = models.IntegerField(primary_key=True)
    number_condition = models.IntegerField(default=0)
    Subject_condition = models.ManyToManyField(Subjectsconditions, related_name="Subjects_Conditions", blank=True)
    Type_condition = models.ForeignKey(Types_Conditions, null = True, blank = True, on_delete=models.CASCADE)
    Number_subject = models.IntegerField()
    All_subjects = models.BooleanField()

    def __str__(self):
        
        return str(f"Id de condiciòn:{self.Id_condition} - Condiciòn:{self.number_condition}")

class Types_Typologys(models.Model):
    Id_typology = models.IntegerField(primary_key=True)  
    Name_typology = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.Name_typology)

class Subject(models.Model):
    Id_subject = models.IntegerField(primary_key=True)
    Name_subject = models.CharField(max_length=100)
    Credits = models.IntegerField()
    Typology = models.ForeignKey(Types_Typologys, null = True, blank = True, on_delete=models.CASCADE)
    Description = models.TextField()
    Id_career = models.ManyToManyField(Career, related_name="Materias")
    Id_condition = models.ManyToManyField(Condition)
    
    def __str__(self):
        return str(f"{self.Id_subject}: {self.Name_subject}")
    
class Group(models.Model):
    Id_group = models.IntegerField(primary_key=True)
    Modality = models.CharField(max_length=40)
    Teacher = models.CharField(max_length=100)
    Date_start = models.DateField()
    Date_finish = models.DateField()
    Duration = models.CharField(max_length=15)
    Working_day = models.CharField(max_length=15)
    Slots = models.IntegerField()
    Id_faculty = models.ManyToManyField(Faculty, related_name='Facultys')
    Id_subject = models.ForeignKey(Subject, null = True, blank = True, on_delete=models.CASCADE)
    Id_schedule = models.ManyToManyField(Schedule, related_name='Schedules')

    def __str__(self):
        return self.Id_group