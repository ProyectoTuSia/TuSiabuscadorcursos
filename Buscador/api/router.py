from rest_framework.routers import DefaultRouter
from Buscador.api.views import CampusApiViewSet
from Buscador.api.views import FacultyApiViewSet
from Buscador.api.views import GroupApiViewSet
from Buscador.api.views import SubjectApiViewSet
from Buscador.api.views import ScheduleApiViewSet
from Buscador.api.views import ConditionApiViewSet
from Buscador.api.views import Types_ConditionsApiViewSet
from Buscador.api.views import PlaceApiViewSet
from Buscador.api.views import CareerApiViewSet

router_campus = DefaultRouter()
router_faculty = DefaultRouter()
router_group = DefaultRouter()
router_subject = DefaultRouter()
router_schedule = DefaultRouter()
router_condition = DefaultRouter()
router_types_conditions = DefaultRouter()
router_place = DefaultRouter()
router_career = DefaultRouter()

router_campus.register(prefix='Campus', basename='Campus', viewset=CampusApiViewSet)
router_faculty.register(prefix='Facultad', basename='Facultad', viewset=FacultyApiViewSet)
router_group.register(prefix='Grupo', basename='Grupo', viewset=GroupApiViewSet)
router_subject.register(prefix='Materia', basename='Materia', viewset=SubjectApiViewSet)
router_schedule.register(prefix='Horario', basename='Horario', viewset=ScheduleApiViewSet)
router_condition.register(prefix='Condicion', basename='Condicion', viewset=ConditionApiViewSet)
router_types_conditions.register(prefix='TipoCondicion', basename='TipoCondicion', viewset=Types_ConditionsApiViewSet)
router_place.register(prefix='Lugar', basename='Lugar', viewset=PlaceApiViewSet)
router_career.register(prefix='Carrera', basename='Carrera', viewset=CareerApiViewSet)
