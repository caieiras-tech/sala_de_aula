from rest_framework import serializers

from aluno.serializers import AlunoSerializer
from professores.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, read_only=True)
    class Meta:
        model = Professor
        fields = ('id', 'nome', 'idade', 'alunos')