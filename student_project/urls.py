
from django.contrib import admin
from django.urls import include, path
from students import views
from students.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.student_form,name="form"),
    path('',views.homepage,name="home"),
    path('enroll/', views.enroll, name="enroll"),
    path('contact/',views.contactUs, name="contact"),
    path('login/',views.Login, name="login"),
    path('about/',views.About, name="about"),
    path('blog/',views.Blog, name="blog"),
    path('logout/', views.logout_view, name='logout'),
    path('form/',views.show_Data,name="form"),

    
    

    

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
