from django.urls import path
from . import views
app_name = 'appfolder'
urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.user_login,name='login'),   # type: ignore
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
]