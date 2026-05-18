from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,                 name='home'),
    path('projects/<int:pk>/',      views.project_detail,       name='project-detail'),
    path('certificates/<int:pk>/',  views.certificate_detail,   name='certificate-detail'),
    path('certificates/<int:pk>/download/', views.certificate_download, name='certificate-download'),
    path('contact/',                views.contact,              name='contact'),
    path('contact/success/',        views.contact_success,      name='contact-success'),
]