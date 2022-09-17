from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet

from Buscador.models import Group
from Buscador.models import Subject
from Buscador.models import Schedule
from Buscador.models import Condition
from Buscador.models import Types_Conditions
from Buscador.models import Place
from Buscador.models import Career
from Buscador.models import Faculty
from Buscador.models import Campus
from Buscador.api.serializers import CampusSerializer
from Buscador.api.serializers import GroupSerializer
from Buscador.api.serializers import SubjectSerializer
from Buscador.api.serializers import ScheduleSerializer
from Buscador.api.serializers import ConditionSerializer
from Buscador.api.serializers import Types_ConditionsSerializer
from Buscador.api.serializers import PlaceSerializer
from Buscador.api.serializers import CareerSerializer
from Buscador.api.serializers import FacultySerializer

from rest_framework.response import Response


class CampusApiViewSet(ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.filter()

    
class GroupApiViewSet(ModelViewSet):
    serializer_class = GroupSerializer    
    queryset = Group.objects.all()
    
class SubjectApiViewSet(ModelViewSet):
    serializer_class = SubjectSerializer  
    queryset = Subject.objects.all()
    
class ScheduleApiViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer  
    queryset = Schedule.objects.all()
    
class ConditionApiViewSet(ModelViewSet):
    serializer_class = ConditionSerializer  
    queryset = Condition.objects.all()
    
class Types_ConditionsApiViewSet(ModelViewSet):
    serializer_class = Types_ConditionsSerializer
    queryset = Types_Conditions.objects.all()
    
class PlaceApiViewSet(ModelViewSet):   
    serializer_class = PlaceSerializer   
    queryset = Place.objects.all()
    
class CareerApiViewSet(ModelViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()
    
class FacultyApiViewSet(ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
    
    