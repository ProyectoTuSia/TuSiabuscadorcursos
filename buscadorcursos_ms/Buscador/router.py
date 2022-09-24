from rest_framework.routers import DefaultRouter
from Buscador.views import CampusApiViewSet
from Buscador.views import FacultyApiViewSet
from Buscador.views import GroupApiViewSet
from Buscador.views import SubjectApiViewSet
from Buscador.views import ScheduleApiViewSet
from Buscador.views import ConditionApiViewSet
from Buscador.views import Types_ConditionsApiViewSet
from Buscador.views import PlaceApiViewSet
from Buscador.views import CareerApiViewSet
from Buscador.views import Types_TypologysApiViewSet
from Buscador.views import SubjectsconditionsApiViewSet
from Buscador.views import IndexCampusApiViewSet
from Buscador.views import IndexFacultyApiViewSet
from Buscador.views import IndexCareerApiViewSet
from Buscador.views import FilteredSubjectsApiVIew

router = DefaultRouter()

router.register(prefix='campus', basename='Campus', viewset=CampusApiViewSet)
router.register(prefix='faculty', basename='Facultad', viewset=FacultyApiViewSet)
router.register(prefix='career', basename='Carrera', viewset=CareerApiViewSet)
router.register(prefix='typetypology', basename='TipoTipologia', viewset=Types_TypologysApiViewSet)
router.register(prefix='subject', basename='Materia', viewset=SubjectApiViewSet)
router.register(prefix='group', basename='Grupo', viewset=GroupApiViewSet)
router.register(prefix='schedule', basename='Horario', viewset=ScheduleApiViewSet)
router.register(prefix='place', basename='Lugar', viewset=PlaceApiViewSet)
router.register(prefix='condition', basename='Condicion', viewset=ConditionApiViewSet)
router.register(prefix='subjectcondition', basename='MateriaCondicional', viewset=SubjectsconditionsApiViewSet)
router.register(prefix='typecondition', basename='TipoCondicion', viewset=Types_ConditionsApiViewSet)

joins = DefaultRouter()
joins.register(prefix='IndexCampus', basename='Index Campus', viewset=IndexCampusApiViewSet)
joins.register(prefix='IndexFaculty', basename='Index Faculty', viewset=IndexFacultyApiViewSet)
joins.register(prefix='IndexCareer', basename='Index Career', viewset=IndexCareerApiViewSet)
joins.register(prefix='IndexSubject', basename='Filtered Subjects', viewset=FilteredSubjectsApiVIew)