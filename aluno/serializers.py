from rest_framework import serializers

from aluno.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields =('id', 'nome', 'idade', 'email')



