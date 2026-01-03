from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name='about_us'),
    path('our-services/', views.our_services, name='our_services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),




    path('newsletter/', views.newsletter, name='newsletter'),
]
