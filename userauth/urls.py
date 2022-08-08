from django.urls import path
from . import views
from .views import *
from django.views.generic import TemplateView


urlpatterns = [

path("", views.home.as_view(), name="Home"),
    #path("list/", ListTheView.as_view()),
    #path("<pk>/update", UpdateTheView.as_view()),
    #path("<pk>/delete", DeleteTheView.as_view()),
    path("you", TemplateView.as_view(template_name='views/home.html')), # django default router
    path('<pk>/reset_password', views.reset_password_view, name='reset_password'),

    path('login/', views.login, name='loginform'),
    path('signup/', views.signup),
    path("editprofile", views.editProfile, name="updateprofile"),
    #Omolola's code below -- tope please fix.
    path("policy", views.policyTest, name="policy"),
]

