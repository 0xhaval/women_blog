from django.urls import path
from . import views


urlpatterns = [
    path('',views.contact,name='contact'),
    path('done/',views.contact_backend,name = 'backend_contact'),
]
