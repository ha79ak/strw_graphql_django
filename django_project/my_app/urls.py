from django.urls import path

from strawberry.django.views import GraphQLView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]