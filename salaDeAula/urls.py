

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from aluno.views import AlunoViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth-api/', obtain_auth_token)
]
