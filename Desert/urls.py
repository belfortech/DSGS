from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name='about_us'),
    path('our-services/', views.our_services, name='our_services'), 
    path('portfolio/', views.portfolio, name='portfolio'), 
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('services/audit-assurance/', views.audit_assurance, name='audit_assurance'),
    path('services/quantification-budgeting/', views.quantification_budgeting, name='quantification_budgeting'),
    path('services/global-financing/', views.global_financing, name='global_financing'),
    path('services/procurement-audit/', views.procurement_audit, name='procurement_audit'),
    path('services/psm-planning/', views.psm_planning, name='psm_planning'),
    path('services/capacity-building/', views.capacity_building, name='capacity_building'),
    path('services/procurement-strategy/', views.procurement_strategy, name='procurement_strategy'),
    path('services/procurement-transformation/', views.procurement_transformation, name='procurement_transformation'),
    path('services/international-business/', views.international_business, name='international_business'),
    



    path('newsletter/', views.newsletter, name='newsletter'),
]