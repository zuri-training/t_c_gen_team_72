from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView

from .models import t_c_Db  # UserModel

from .models import t_c_Db, PrivacyPolicyQuestions, Terms_and_condition
from django.contrib.auth.models import User, auth

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages

from django.http import HttpResponse

from . import forms


class CreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'index.html'
    success_url = 'list'


class ListTheView(ListView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    template_name = 'listView.html'

    def my_view(self, request):
        if not request.user.is_authenticated:
            return redirect('%s?next=s%' % (settings.Login_url, request.path))


# Omolola's code below -- tope please fix.
def policyTest(request):
    return render(request, "policy.html")


class home(TemplateView):
    template_name = "index.html"

# resets the password
@login_required
def reset_password_view(request, pk):
    form = forms.ResetPassword()

    # Check to see if we get a POST back
    if request.method == "POST":
        form = forms.ResetPassword(request.POST)

        if form.is_valid():
            pass
    return render(request, 'reset_password.html', {'form': form})


# controls the user signup

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


# View for edit profile
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
            error = error + 1
        else:
            email = request.POST['email']

        if not request.POST['company']:
            messages.error(request, 'company field is required')
            error = error + 1
        else:
            company = request.POST['company']

        if not request.POST['business']:
            messages.error(request, 'Firstname field is required')
            error = error + 1
        else:
            business = request.POST['business']

        if not request.POST['address']:
            messages.error(request, 'address field is required')
            error = error + 1
        else:
            address = request.POST['address']

        if not request.POST['number']:
            messages.error(request, 'number field is required')
            error = error + 1
        else:
            number = request.POST['number']

        if error > 0:
            return redirect("updateprofile")
        else:
            # call the user detail from appropriate table using the users id e.g
            myuser = User.objects.get(pk=id)
            # input the above data into the database e.g myuser.company = company
            myuser.save()
            messages.success(request, "Your account has been updated successfully")
            return redirect('dashboard')
    else:
        return render(request, "editprofile.html")


def reset_password_view(request, pk):
    form = forms.ResetPassword()

    # Check to see if we get a POST back
    if request.method == "POST":
        form = forms.ResetPassword(request.POST)

        if form.is_valid():
            pass
    return render(request, 'reset_password.html', {'form': form})


""""
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('me')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/signup')



    else:
        return render(request, 'loginform.html')

"""


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'success')
        return redirect('me')
    return render(request, 'sign_up.html')


#############################################
class TermsPoliciesView(ListView):  # list the texts inserted into the database into the html file created here
    model = PrivacyPolicyQuestions
    template_name = 'generate.html'

    def terms_policies(self, request):
        new_user = t_c_Db.objects.all().values()
        args = {'new_user': new_user}
        return render(request, 'generate.html', args)


class NewCreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'create.html'
    success_url = 'list'


def question1(request):
    if request.method == "POST":
        construction = request.POST["browser"]
        if construction == "Construction":
            user = PrivacyPolicyQuestions(construction="True")


            user.save()
        elif construction == "Finance":
            user = PrivacyPolicyQuestions(finance="True")
            user.save()
        elif construction == "Employment":
            user = PrivacyPolicyQuestions(employment="True")
            user.save()
        elif construction == "Freelancer":
            user = PrivacyPolicyQuestions(freelancer="True")
            user.save()
        elif construction == "SAAS":
            user = PrivacyPolicyQuestions(saas="True")
            user.save()
        elif construction == "Health Care":
            user = PrivacyPolicyQuestions(health_care="True")
            user.save()
        elif construction == "Real estate":
            user = PrivacyPolicyQuestions(real_estate="True")
            user.save()
        return render(request, 'gene.html', {'user': user})

    else:
        pass
    return render(request, '1collection.html')


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
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('loginform')




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
        return redirect('/me')
    return render(request, 'sign_up.html')


def contact_us(request):
    return render(request, 'contact.html')


def question(request):
    return render(request, 'privacypolicy.html')


def question2(request):
    return render(request, 'user_info.html')


def question3(request):
    if request.method == "POST":
        construction = request.POST["browser"]
        if construction == "Construction":
            user = PrivacyPolicyQuestions.objects.get(id=3)
            print(user)
            user = PrivacyPolicyQuestions(construction="True")
            #            user.save(update_fields=["construction"])
            user.save()
        elif construction == "Finance":
            user = PrivacyPolicyQuestions(finance="True")
            user.save()
        elif construction == "Employment":
            user = PrivacyPolicyQuestions(employment="True")
            user.save()
        elif construction == "Freelancer":
            user = PrivacyPolicyQuestions(freelancer="True")
            user.save()
        elif construction == "SAAS":
            user = PrivacyPolicyQuestions(saas="True")
            user.save()
        elif construction == "Health Care":
            user = PrivacyPolicyQuestions(health_care="True")
            user.save()
        elif construction == "Real estate":
            user = PrivacyPolicyQuestions(real_estate="True")
            user.save()
        return render(request, 'collection-two.html', {'user': user})

    else:
        pass
    return render(request, 'one-collection.html')


def question4(request):
    return render(request, 'collection-two.html')


def generate(request):
    return render(request, 'generate.html')


def dashboard(request):
    return render(request, 't-c-preview.html')


def about_us(request):
    return render(request, 'about-us.html')


def faq(request):
    return render(request, 'security_faqs.html')


def policy(request):
    return render(request, 'policy.html')


