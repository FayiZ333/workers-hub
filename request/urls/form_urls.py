from django.urls import path, include
from .. import views

urlpatterns = [

    path('form/', views.FormView.as_view(), name='form'),

]