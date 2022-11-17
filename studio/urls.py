from django.urls import path

from django.views.generic.base import TemplateView

from studio import views

urlpatterns = [
        path('',views.IndexView.as_view()),
        path('contact/', views.ContactView.as_view(), name = 'contact'),
    
] 