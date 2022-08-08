from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView

from django.contrib.auth.models import User, auth

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages

from django.http import HttpResponse


from . import forms

#Omolola's code below -- tope please fix.
def policyTest(request):
    return render(request, "policy.html")

class home(TemplateView):
    template_name = "landingPage.html"

@login_required
def reset_password_view(request, pk):
    form = forms.ResetPassword()

    # Check to see if we get a POST back
    if request.method == "POST":
        form = forms.ResetPassword(request.POST)

        if form.is_valid():
            pass
    return render(request, 'reset_password.html', {'form': form})

#Login authenticatin and request

def login(request):
    if request.method == 'POST':

        error = 0
        # To check if username is not empty
        if not request.POST['username']:
            messages.error(request, 'Username field is required')


        else:
            username = request.POST['username']
            print(username)

        # To check if password is not empty
        if not request.POST['password']:
            messages.error(request, 'Password field is required')

        else:
            password = request.POST['password']

        # if password and or password is null, redirected to login passage with erroe message

        if error > 0:
            return redirect('/login')

        else:

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You are successfully logged in")
                return redirect('home')
            else:
               messages.error(request, 'Invalid Username or Password')

    else:
        if request.user.is_authenticated:
            redirect("Home")
        else:
            return render(request, 'loginform.html')


#Login authenticatin and request
def signup(request):
    if request.method == "POST":
        error = 0
        # To check if username is not empty
        if not request.POST['username']:
            messages.info(request, 'Username field is required')
            error = error + 1
        else:
            username = request.POST['username']

        # To check if password is not empty
        if not request.POST['password']:
            messages.info(request, 'Password field is required')
            error = error + 1
        else:
            password = request.POST['password']

        # To check if email is not empty
        if not request.POST['email']:
            messages.info(request, 'Email field is required')
            error = error + 1
        else:
            email = request.POST['email']


        # if password and or password is null, redirected to registration page with error message

        if error > 0:
            return redirect('/register')
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'success')
            return redirect('/list')
    else:
        if request.user.is_authenticated:
            redirect("Home")
        else:
            return render(request, 'sign_up.html')

#View for edit profile
@login_required
def editProfile(request, id):
    if request.method == "POST":
        error = 0
        # To check if username is not empty
        if not request.POST['name']:
            messages.error(request, 'name field is required')
            error = error + 1
        else:
            username = request.POST['name']

        if not request.POST['email']:
            messages.error(request, 'Email field is required')
            error = error +1
        else:
            email = request.POST['email']

        if not request.POST['company']:
            messages.error(request, 'company field is required')
            error = error +1
        else:
            company  = request.POST['company']

        if not request.POST['business']:
            messages.error(request, 'Firstname field is required')
            error = error +1
        else:
            business = request.POST['business']

        if not request.POST['address']:
            messages.error(request, 'address field is required')
            error = error +1
        else:
            address = request.POST['address']

        if not request.POST['number']:
            messages.error(request, 'number field is required')
            error = error +1
        else:
            number = request.POST['number']

        if error > 0:
            return redirect("updateprofile")
        else:
            #call the user detail from appropriate table using the users id e.g
            myuser=User.objects.get(pk=id)
            #input the above data into the database e.g myuser.company = company
            myuser.save()
            messages.success(request, "Your account has been updated successfully")
            return redirect('dashboard')
    else:
        return render(request, "editprofile.html")

"""
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
    """


# Create your views here.




