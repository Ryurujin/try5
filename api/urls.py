from django.urls import path, include
from .views import *

urlpatterns = [
    #user
    path('user/', User_views_list),
    path('user/<int:pk>/', User_views_detail),

    #project
    path('project/', Project_views_list),
    path('project/<int:pk>/', Project_views_detail), 

    #task
    path('task/', Task_views_list),
    path('task/<int:pk>/', Task_views_detail), 

    path('auth/', include('dj_rest_auth.urls')),

]