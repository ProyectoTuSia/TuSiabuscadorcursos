from gzip import READ
from http.client import REQUEST_ENTITY_TOO_LARGE
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Buscador.models import Campus
from Buscador.models import Faculty


@api_view(['GET', 'PUT'])
def filterCourses(request):
    #traerse los modelos necesarios y hacer las consultas, tal vez con JOINS
    
    return Response({"unu": request.data})
