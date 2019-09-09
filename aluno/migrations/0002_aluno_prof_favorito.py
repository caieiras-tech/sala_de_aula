# Generated by Django 2.2.5 on 2019-09-09 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0001_initial'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='prof_favorito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='professores.Professor'),
            preserve_default=False,
        ),
    ]