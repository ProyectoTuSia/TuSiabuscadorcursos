from rest_framework.serializers import ModelSerializer
from Buscador.models import Group
from Buscador.models import Subject
from Buscador.models import Schedule
from Buscador.models import Condition
from Buscador.models import Types_Conditions
from Buscador.models import Place
from Buscador.models import Career
from Buscador.models import Faculty
from Buscador.models import Campus

class CampusSerializer(ModelSerializer):
    class Meta:
        model = Campus
        fields = ['Id_campus', 'Name_campus']
        
class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['Id_faculty', 'Name_faculty', 'Id_campus']

class CareerSerializer(ModelSerializer):
    class Meta:
        model = Career
        fields = ['Id_career', 'Name_career', 'Id_faculty']

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ['Id_place', 'Place_tower', 'Place_salon']

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['Id_schedule', 'Star_time', 'End_time', 'Id_place']

class Types_ConditionsSerializer(ModelSerializer):
    class Meta:
        model = Types_Conditions
        fields = ['Id_types', 'Description']

class ConditionSerializer(ModelSerializer):
    class Meta:
        model = Condition
        fields = ['Id_condition', 'Subject_condition', 'Type_condition', 'Number_subject', 'All_subjects']
        
class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['Id_subject', 'Name_subject', 'Credits', 'Typology', 'Description', 'Id_career', 'Id_condition']
    
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['Id_group', 'Modality', 'Teacher', 'Date_start', 'Date_finish', 'Duration', 'Working_day', 'Slots', 'Id_faculty', 'Id_subject', 'Id_sheduler']
        
