

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from aluno.views import AlunoViewSet, AlunoList, AlunoDetails
from professores.views import ProfessorViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)


urlpatterns = [
    path('alunos', AlunoList.as_view()),
    path('alunos/<int:id>', AlunoDetails.as_view()),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth-api/', obtain_auth_token)
]
