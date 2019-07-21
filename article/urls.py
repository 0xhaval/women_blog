from . import views
from django.urls import path

urlpatterns = [
    path('',views.test,name='article'),
    path("<slug:slug>/", views.article_detail,name='detail'),
]
