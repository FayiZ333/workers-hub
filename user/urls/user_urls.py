from django.urls import path, include
from .. import views

urlpatterns = [

    path('forgot/', views.ForgotView.as_view(), name='forgot'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]

