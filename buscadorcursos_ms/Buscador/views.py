from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from Buscador.models import Group,  Subject, Schedule, Condition, Types_Conditions, Place, Career, Faculty, Campus, Types_Typologys, Subjectsconditions
from Buscador.serializers import CampusSerializer, GroupSerializer, SubjectSerializer, ScheduleSerializer, Types_TypologysSerializer
from Buscador.serializers import ConditionSerializer, Types_ConditionsSerializer, PlaceSerializer, CareerSerializer, FacultySerializer
from Buscador.serializers import SubjectsconditionsSerializer, IndexCampusSerializer, IndexFacultySerializer, IndexCareerSerializer
from rest_framework.response import Response


class CampusApiViewSet(ModelViewSet):
    serializer_class = CampusSerializer
    def get_queryset(self):
        queryset = Campus.objects.filter()
        return queryset
    
    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                campus = Campus.objects.get(id=id)
                serializer = CampusSerializer(campus)
        except:
            campus = self.get_queryset()
            serializer = CampusSerializer(campus, many=True)

        return Response(serializer.data)
    
class FacultyApiViewSet(ModelViewSet):
    serializer_class = FacultySerializer
    def get_queryset(self):
        faculty = Faculty.objects.all()
        return faculty

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                faculty = Faculty.objects.get(id=id)
                serializer = FacultySerializer(faculty)
        except:
            faculty = self.get_queryset()
            serializer = FacultySerializer(faculty, many=True)

        return Response(serializer.data)
class CareerApiViewSet(ModelViewSet):
    serializer_class = CareerSerializer
    def get_queryset(self):
        career = Career.objects.all()
        return career

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                career = Career.objects.get(id=id)
                serializer = CareerSerializer(career)
        except:
            career = self.get_queryset()
            serializer = CareerSerializer(career, many=True)

        return Response(serializer.data)   
    
class PlaceApiViewSet(ModelViewSet):   
    serializer_class = PlaceSerializer   
    def get_queryset(self):
        place = Place.objects.all()
        return place

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                place = Place.objects.get(id=id)
                serializer = PlaceSerializer(place)
        except:
            place = self.get_queryset()
            serializer = PlaceSerializer(place, many=True)

        return Response(serializer.data)
    
class GroupApiViewSet(ModelViewSet):
    serializer_class = GroupSerializer    
    def get_queryset(self):
        group = Group.objects.all()
        return group

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                group = Group.objects.get(id=id)
                serializer = GroupSerializer(group)
        except:
            group = self.get_queryset()
            serializer = GroupSerializer(group, many=True)
            
        return Response(serializer.data)
    
class SubjectApiViewSet(ModelViewSet):
    serializer_class = SubjectSerializer  
    def get_queryset(self):
        subject = Subject.objects.all()
        return subject

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                subject = Subject.objects.get(id=id)
                serializer = SubjectSerializer(subject)
        except:
            subject = self.get_queryset()
            serializer = SubjectSerializer(subject, many=True)
    
        return Response(serializer.data)
class ScheduleApiViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer  
    def get_queryset(self):
        schedule = Schedule.objects.all()
        return schedule

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                schedule = Schedule.objects.get(id=id)
                serializer = ScheduleSerializer(schedule)
        except:
            schedule = self.get_queryset()
            serializer = ScheduleSerializer(schedule, many=True)
        
        return Response(serializer.data)
    
class ConditionApiViewSet(ModelViewSet):
    serializer_class = ConditionSerializer  
    def get_queryset(self):
        condition = Condition.objects.all()
        return condition

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                car = Condition.objects.get(id=id)
                serializer = ConditionSerializer(car)
        except:
            condition = self.get_queryset()
            serializer = ConditionSerializer(condition, many=True)

        return Response(serializer.data)
    
class Types_ConditionsApiViewSet(ModelViewSet):
    serializer_class = Types_ConditionsSerializer
    def get_queryset(self):
        types_Conditions = Types_Conditions.objects.all()
        return types_Conditions

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                types_Conditions = Types_Conditions.objects.get(id=id)
                serializer = Types_ConditionsSerializer(types_Conditions)
        except:
            types_Conditions = self.get_queryset()
            serializer = Types_ConditionsSerializer(types_Conditions, many=True)

        return Response(serializer.data)
     
class Types_TypologysApiViewSet(ModelViewSet):
    serializer_class = Types_TypologysSerializer
    def get_queryset(self):
        types_Typologys = Types_Typologys.objects.all()
        return types_Typologys

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                types_Typologys = Types_Typologys.objects.get(id=id)
                serializer = Types_TypologysSerializer(types_Typologys)
        except:
            types_Typologys = self.get_queryset()
            serializer = Types_TypologysSerializer(types_Typologys, many=True)

        return Response(serializer.data)
    
class SubjectsconditionsApiViewSet(ModelViewSet):
    serializer_class = SubjectsconditionsSerializer
    def get_queryset(self):
        subjectsconditions = Subjectsconditions.objects.all()
        return subjectsconditions

    def get(self, request, *args, **kwargs):
        
        try:
            id = request.query_params["id"]
            if id != None:
                subjectsconditions = Subjectsconditions.objects.get(id=id)
                serializer = SubjectsconditionsSerializer(subjectsconditions)
        except:
            subjectsconditions = self.get_queryset()
            serializer = SubjectsconditionsSerializer(subjectsconditions, many=True)

        return Response(serializer.data)
    
class GroupsforSubjectApiViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    groupsforsubject = Group.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Id_subject']

class IndexCareerApiViewSet(ModelViewSet): 
    serializer_class = IndexCareerSerializer
    queryset=Career.objects.filter(Id_career=2879)
class IndexFacultyApiViewSet(ModelViewSet): 
    serializer_class = IndexFacultySerializer
    queryset=Faculty.objects.filter(Id_faculty=2055)

class IndexCampusApiViewSet(ModelViewSet): 
    serializer_class = IndexCampusSerializer
    queryset=Campus.objects.filter(pk=1101)
    
class FilteredSubjectsApiVIew(ModelViewSet):
    queryset=Subject.objects.defer("Id_subject", "Name_subject", "Credits", "Typology", "Description")
    serializer_class = SubjectSerializer

    