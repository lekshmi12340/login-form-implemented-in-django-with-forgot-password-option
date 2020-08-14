from django.urls import path
from . import views
urlpatterns=[
             # path('home',views.home,name="home"),
             path('signup', views.signup, name="signup"),
             path('login', views.login, name="login"),
             path('resetpasswords', views.resetpasswords, name="resetpasswords"),
             path('logout', views.logout, name="logout"),
             path('redirects', views.redirects, name="redirects"),


]