
from django.http import HttpResponse, JsonResponse
from .models import Editorial, Libro, Persona, Prestamo
from rest_framework import viewsets
from .serializers import EditorialSerializer
from .serializers import LibroSerializer
from .serializers import PersonaSerializer
from .serializers import PrestamoSerializer
# Create your views here.
def hello(request):
    return HttpResponse("Hello World Edwin")
def about(request):
    return HttpResponse("about")

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
