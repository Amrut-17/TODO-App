from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('add-task/', views.add_task, name='addtask'),
    path('delete-task/<int:id>', views.delete_task, name='deletetask'),
]
