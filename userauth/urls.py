from django.urls import path
from . import views
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView, logintest, testView, policyTest, LoggedUser
from .views import CreateViewQuestions, ListViewQuestions, TermsPoliciesView, NewCreateView
from django.views.generic import TemplateView
from .models import t_c_Db

new_user = t_c_Db.description
args = {'new_user': new_user}

urlpatterns = [

    path("", views.CreateView.as_view(), name="Home"),
    path("list/", ListTheView.as_view()),
    path("<pk>/update", UpdateTheView.as_view()),
    path("<pk>/delete", DeleteTheView.as_view()),
    path("you", TemplateView.as_view(template_name='views/home.html')), # django default router
    path('<pk>/reset_password', views.reset_password_view, name='reset_password'),
    path("edit", views.testView, name="edit"),
    path("login", views.logintest,  name="login"),
    path('login/', views.login, name='loginform'),
    path('signup/', views.signup),
    path('me/', TermsPoliciesView.as_view(), args),
    path('details/', LoggedUser.as_view()),
    #Omolola's code below -- tope please fix.
    path("policy", views.policyTest, name="policy"),
    #######################################
    path('Create', NewCreateView.as_view()),
    path('create/', CreateViewQuestions.as_view()),
    path('me/questions', ListViewQuestions.as_view()),
#   path('generate/', #NewLoggedUser.as_view(), {'get_id': get_id}),
    path('question1', views.question1)

]

