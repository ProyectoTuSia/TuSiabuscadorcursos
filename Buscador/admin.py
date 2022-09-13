from django.contrib import admin
from Buscador.models import Group
from Buscador.models import Subject
from Buscador.models import Schedule
from Buscador.models import Condition
from Buscador.models import Types_Conditions
from Buscador.models import Place
from Buscador.models import Career
from Buscador.models import Faculty
from Buscador.models import Campus
# Register your models here.

admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Condition)
admin.site.register(Types_Conditions)
admin.site.register(Place)
admin.site.register(Career)
admin.site.register(Faculty)
admin.site.register(Campus)
