from django.urls import path
from . import views

app_name = "passGen"
urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('generate', views.IndexView.generate, name='generate'),
]