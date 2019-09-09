from django.shortcuts import render
from rest_framework import viewsets

from professores.models import Professor
from professores.serializers import ProfessorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

