from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home',TemplateView.as_view(template_name='index.html')),
]
