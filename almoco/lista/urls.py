from django.urls import path
from .views import solicitar, registros

urlpatterns = [
    path('solicitar/', solicitar, name='solicitar'),
    path('registros/', registros, name='registros'),
]