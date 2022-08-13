from django.urls import path

from .views import CreateView, policyTest, ListTheView
from .views import TermsPoliciesView, NewCreateView

from .views import CreateView, policyTest

from . import views

from django.views.generic import TemplateView
from .models import t_c_Db

new_user = t_c_Db.description
args = {'new_user': new_user}

urlpatterns = [

    path("", views.CreateView.as_view(), name="Home"),

    path("", views.CreateView.as_view(), name="Home"),

    path("", views.CreateView.as_view(), name="Home"),
    path("list/", TermsPoliciesView.as_view()),

    path("", views.CreateView.as_view(), name="Home"),
    # path("list/", ListTheView.as_view()),

    path("", views.home.as_view(), name="Home"),
    # path("list/", ListTheView.as_view()),

    # path("<pk>/update", UpdateTheView.as_view()),
    # path("<pk>/delete", DeleteTheView.as_view()),

    path("you", TemplateView.as_view(template_name='views/home.html')),  # django default router
    path('<pk>/reset_password', views.reset_password_view, name='reset_password'),

    path('login/', views.login, name='loginform'),
    path('signup/', views.signup, name='signup'),
    path('me/', views.dashboard, name='dashboard'),

    path("editprofile", views.editProfile, name="updateprofile"),

    # Omolola's code below -- tope please fix.

    path("policy", views.policyTest, name="policy"),
    #######################################
    path('Create', NewCreateView.as_view()),

    #   path('generate/', #NewLoggedUser.as_view(), {'get_id': get_id}),

    path("policy", views.policy, name="policy"),
    path("faq", views.faq, name="faq"),

    path("contact-us", views.contact_us, name="contact-us"),
    path("about-us", views.about_us, name="about-us"),
    path("question/1", views.question, name="first_question"),
    path("question/2", views.question2, name="second_question"),
    path("question/3", views.question3, name="third_question"),
    path("question/4", views.question4, name="fourth_question"),
    path("terms and condition/export", TermsPoliciesView.as_view(), name="export"),
]
