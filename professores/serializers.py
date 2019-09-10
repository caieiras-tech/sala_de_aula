from rest_framework import serializers

from aluno.serializers import AlunoSerializer
from professores.models import Professor


class ProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    alunos_professor = AlunoSerializer(many=True, required=False)

    def create(self, validated_data):
        return Professor.objects.create(**validated_data)