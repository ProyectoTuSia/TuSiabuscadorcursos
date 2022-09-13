from pyexpat import model
from django.db import models

# Create your models here.
class Campus(models.Model):
    Id_campus = models.IntegerField(primary_key=True)
    Name_campus = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Name_campus

class Faculty(models.Model):
    Id_faculty = models.IntegerField(primary_key=True)
    Name_faculty = models.CharField(max_length=50)
    Id_campus = models.ForeignKey(Campus, null = True, blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name_faculty

class Career(models.Model):
    Id_career = models.IntegerField(primary_key=True)
    Name_career = models.CharField(max_length=50)
    Id_faculty = models.ForeignKey(Faculty, null = True, blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name_career
    
class Place(models.Model):
    Id_place = models.IntegerField(primary_key=True)
    Place_tower = models.TextField()
    Place_salon = models.TextField()
    
    def __str__(self):
        return self.Id_place
        
class Schedule(models.Model):
    Id_schedule = models.IntegerField(primary_key=True)
    Star_time = models.DateField()
    End_time = models.DateField()
    Id_place = models.ForeignKey(Place, null = True, blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.Id_schedule
    
class Types_Conditions(models.Model):
    Id_types = models.CharField(max_length=5, primary_key=True)
    Description = models.TextField()
    
    def __str__(self):
        return self.Id_types
    
class Condition(models.Model):
    Id_condition = models.IntegerField(primary_key=True)
    Subject_condition = models.IntegerField()
    Type_condition = models.ForeignKey(Types_Conditions, null = True, blank = True, on_delete=models.CASCADE)
    Number_subject = models.IntegerField()
    All_subjects = models.BooleanField()

    def __str__(self):
        return self.Id_condition
    
class Subject(models.Model):
    Id_subject = models.IntegerField(primary_key=True)
    Name_subject = models.CharField(max_length=50)
    Credits = models.IntegerField()
    Typology = models.CharField(max_length=20)
    Description = models.TextField()
    Id_career = models.ManyToManyField(Career)
    Id_condition = models.ManyToManyField(Condition)
    
    def __str__(self):
        return self.Name_subject
    
class Group(models.Model):
    Id_group = models.IntegerField(primary_key=True)
    Modality = models.CharField(max_length=30)
    Teacher = models.CharField(max_length=50)
    Date_start = models.DateField()
    Date_finish = models.DateField()
    Duration = models.CharField(max_length=15)
    Working_day = models.CharField(max_length=15)
    Slots = models.IntegerField()
    Id_faculty = models.IntegerField()
    Id_subject = models.ForeignKey(Subject, null = True, blank = True, on_delete=models.CASCADE)
    Id_sheduler = models.ManyToManyField(Schedule)

    def __str__(self):
        return self.Id_group