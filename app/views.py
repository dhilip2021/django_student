from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer

# Create your views here.
def index(request):
    obj = Student.objects.all()
    return render(request, 'index.html',{'obj':obj})

class StuidentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset= Student.objects.all()
