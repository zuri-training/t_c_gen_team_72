from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import t_c_Db
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.conf import settings
from django.contrib import messages

from django.http import HttpResponse


from . import forms


def testView(request):
    return render(request, "editprofile.html")
def logintest(request):
    return render(request, "loginform.html")
#Omolola's code below -- tope please fix.
def policyTest(request):
    return render(request, "policy.html")




class CreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'landingPage.html'
    success_url = 'list'


class ListTheView(ListView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    template_name = 'listView.html'
    def my_view(self, request):
        if not request.user.is_authenticated:
            return redirect('%s?next=s%' % (settings.Login_url, request.path))


# Create your views here.


class UpdateTheView(UpdateView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'Update.html'
    success_url = '/'


class DeleteTheView(DeleteView):
    model = t_c_Db
    template_name = 'Delete.html'
    success_url = '/'



# Create your views here.

def reset_password_view(request, pk):
    form = forms.ResetPassword()

    # Check to see if we get a POST back
    if request.method == "POST":
        form = forms.ResetPassword(request.POST)

        if form.is_valid():
            pass
    return render(request, 'reset_password.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/list')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/signup')



    else:
        return render(request, 'loginform.html')





def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'success')
        return redirect('/list')
    return render(request, 'sign_up.html')








