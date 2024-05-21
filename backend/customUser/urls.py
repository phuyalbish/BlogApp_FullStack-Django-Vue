from django.urls import  path
from customUser import views



urlpatterns = [

    path('register/', views.register),
    path('logins/', views.logins, name='loginView'),
    path('updateUser/', views.updateUser, name='loginView'),
    path('checkToken/', views.checkToken),
    path('checkMailAvailable/', views.checkMailAvailable, name="checkMail")

    # path('users/', views.get, name="getData"),
    # path('user/<int:userid>/', views.getUser, name="getUserData"),
    # path('user/edit/<int:userid>/', views.patch, name="patchData"),
    # path('user/checkMailAvailable/', views.checkMailAvailable, name="checkMailAvailable"),
]