
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('new_page/',views.new_page,name='new_page'),
    path('application_accepted/',views.application_accepted,name='application_accepted'),
    path('district_wiki/<int:district_id>/', views.district_wiki, name='district_wiki'),

]


