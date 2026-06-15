from django.contrib import admin
from django.urls import include, path

from .import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('reg/',views.register),
    path('saveform/', views.saveform, name='saveform'),
    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('update/<int:id>/', views.updatestudent, name='update'),
    path('deletestudent/<int:id>/', views.deletestudent, name='delete'),
    path("login/", views.login, name="login"),
    path("logincheck/", views.logincheck, name="logincheck"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("add_cookie/", views.add_cookie, name="add_cookie"),
    path("view_cookie/", views.view_cookie, name="view_cookie"),
    path("fileupload/", views.file_upload, name="file_upload"),
    path("file/", views.file, name="file"),
    path("form/", views.form, name="form")
    
   
    

   
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('reg/', views.register, name='register'),
#     path('saveform/', views.saveform, name='saveform'),
#     path('viewstudent/', views.viewstudent, name='viewstudent'),
#     path('delete/<int:id>/', views.deletestudent, name='deletestudent'),
#     path('update/<int:id>/', views.updatestudent, name='updatestudent'),

#     path('login/', views.login, name='login'),
#     path('logincheck/', views.logincheck, name='logincheck'),
#     path('dashboard/', views.dashboard, name='dashboard'),

#     path('logout/', views.user_logout, name='logout'),
# ]
