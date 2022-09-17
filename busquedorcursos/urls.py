"""busquedorcursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Buscador.api.router import router_campus, router_faculty, router_group, router_subject, router_schedule, router_condition, router_types_conditions, router_place, router_career

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filtrador/', include('Buscador.urls')),
    path('sede/', include('Buscador.urls')),
    path('apicampus/', include(router_campus.urls)),
    path('apifaculty/', include(router_faculty.urls)),
    path('apigroup/', include(router_group.urls)),
    path('apisubject/', include(router_subject.urls)),
    path('apischedule/', include(router_schedule.urls)),
    path('apicondition/', include(router_condition.urls)),
    path('apitypescondition/', include(router_types_conditions.urls)),
    path('apiplace/', include(router_place.urls)),
    path('apicareer/', include(router_career.urls)),

    path('buscadorCursos', include("Buscador.urls"))
]
