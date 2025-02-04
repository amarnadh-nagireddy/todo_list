from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('new_task/',views.new_task,name="new_task"),
    path('modify_task/<int:id>/',views.modify_task,name="modify_task"),
    path('delete_task/<int:id>/',views.delete_task,name="delete_task"),
    path('completed_task/<int:id>/',views.completed_task,name='completed_task')
   
]