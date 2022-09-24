from re import T
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Buscador.models import Group,  Subject, Schedule, Condition, Types_Conditions, Place, Career, Faculty, Campus, Types_Typologys, Subjectsconditions

class CareerSerializer(ModelSerializer):
    Id_faculty = serializers.SlugRelatedField(queryset=Faculty.objects.all(), slug_field='Name_faculty')
    class Meta:
        model = Career
        fields = ['Id_career', 'Name_career', 'Id_faculty']
    
class FacultySerializer(ModelSerializer):
    Id_campus = serializers.SlugRelatedField(queryset=Campus.objects.all(), many=True, slug_field='Name_campus')
    class Meta:
        model = Faculty
        fields = ['Id_faculty', 'Name_faculty', 'Id_campus']

class CampusSerializer(ModelSerializer):
    class Meta:
        model = Campus
        fields = ['Id_campus', 'Name_campus']
        
        
class SubjectsconditionsSerializer(ModelSerializer):
    class Meta:
        model = Subjectsconditions
        fields = ['Id_Subjectconditions', 'Name_subjectconditions']
        
        
class CareerSerializer(ModelSerializer):
    Id_faculty = serializers.SlugRelatedField(queryset=Faculty.objects.all(), slug_field='Name_faculty')
    class Meta:
        model = Career
        fields = ['Id_career', 'Name_career', 'Id_faculty']

class PlaceSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = ['Id_place', 'Place_numbertower', 'Place_nametower',  'Place_numbersalon', 'Place_namesalon']
        
        
class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['Id_Schedule','day_name', 'Star_time', 'End_time', 'Id_place']


class Types_ConditionsSerializer(ModelSerializer):
    class Meta:
        model = Types_Conditions
        fields = ['Id_types', 'Description']

class ConditionSerializer(ModelSerializer):
    Type_condition = serializers.SlugRelatedField(queryset=Types_Conditions.objects.all(), slug_field='Id_types')
    Subject_condition = serializers.SlugRelatedField(queryset=Subjectsconditions.objects.all(), slug_field='Name_subjectconditions', many=True)
    class Meta:
        model = Condition
        fields = ['Id_condition', 'number_condition','Subject_condition', 'All_subjects', 'Number_subject', 'Type_condition']

class Types_TypologysSerializer(ModelSerializer):
    class Meta:
        model = Types_Typologys
        fields = ['Id_typology', 'Name_typology']
        
class SubjectSerializer(ModelSerializer):
    Id_career = serializers.SlugRelatedField(queryset=Career.objects.all(), slug_field='Name_career', many=True)
    class Meta:
        model = Subject
        fields = ['Id_subject', 'Name_subject', 'Credits', 'Typology', 'Description', 'Id_career', 'Id_condition']
    
class GroupSerializer(ModelSerializer):
    Id_faculty = serializers.SlugRelatedField(queryset=Faculty.objects.all(), slug_field='Name_faculty', many=True)
    class Meta:
        model = Group
        fields = ['Id_group', 'Modality', 'Teacher', 'Date_start', 'Date_finish', 'Duration', 'Working_day', 'Slots', 'Id_faculty', 'Id_subject', 'Id_schedule']
    
    
# <------------------------------------------------------------------------------------------------>
class IndexCareerSerializer(ModelSerializer):
    Id_faculty = serializers.SlugRelatedField(queryset=Faculty.objects.all(), slug_field='Name_faculty')
    Materias = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Career
        fields = ['Id_career', 'Name_career', 'Id_faculty', 'Materias']
    
class IndexFacultySerializer(ModelSerializer):
    Id_campus = serializers.SlugRelatedField(queryset=Campus.objects.all(), many=True, slug_field='Name_campus')
    Careers = IndexCareerSerializer(many=True, read_only=True)
    class Meta:
        model = Faculty
        fields = ['Id_faculty', 'Name_faculty', 'Id_campus', 'Careers']
        
class IndexCampusSerializer(ModelSerializer):
    Facultys =  IndexFacultySerializer(many=True, read_only=True)
    class Meta:
        model = Campus
        fields = ['Id_campus', 'Name_campus', 'Facultys']
        

        
        