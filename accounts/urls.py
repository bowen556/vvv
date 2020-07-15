from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('locations/', views.locations, name="locations"),
    path('viewlocations/<str:pk>/', views.viewlocations, name="viewlocations"),
    path('users/', views.users, name="users"),
    path('admin/auth/user/add/', views.createUsers, name="create_users"),
    path('admin/accounts/entry/add/', views.createLocations, name="create_locations"),
    path('login/', views.loginPage, name="login"),
    path('login2/', views.login2, name="login2"),
    path('login3/', views.login3, name="login3"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_profile/', views.userProfile, name="profile"),
    path('region/<str:cats>/', views.Region, name="region"),
    path('allregions/', views.allRegions, name="allregions"),


]