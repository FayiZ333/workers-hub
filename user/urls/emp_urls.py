from django.urls import path, include
from .. import views

urlpatterns = [

    path('reg/', views.EmpIdView.as_view(), name='reg'),

]

