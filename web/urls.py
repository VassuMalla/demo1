from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('home/',views.home,name='home'),
    path('trainers/',views.trainers,name='trainers'),
    path('courses/',views.courses,name='courses'),
    path('contact/',views.contact,name='contact'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('detail/',views.detail,name='detail'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_view,name='logout'),
]
