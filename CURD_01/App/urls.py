from django.urls import path
from .import views

urlpatterns = [
    path('', views.SignUp, name='SignUp'),
    path('login/', views.LogIn, name='LogIn'),
    path("notebook/", views.Notebook, name='Notebook'),
    path('logout/', views.LogOut, name='LogOut'),
    path('changepassword/', views.PasswordChange, name='ChangePassword'),
    path("notebook/showallnotes/", views.ShowAllNotes, name='ShowAllNotes'),
    path('notebook/showallnotes/editdata/<int:id>/', views.EditNote, name='EditNote'),
    path('delete/<int:id>/', views.Delete, name='Delete'),
]
