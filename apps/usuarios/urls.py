from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    
    path('bienvenida/', views.BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', views.SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', views.SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', views.SignOutView.as_view(), name='sign_out'),
]
