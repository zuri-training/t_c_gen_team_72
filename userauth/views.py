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
""""
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

"""

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
<<<<<<< HEAD
    model = Questions
||||||| f761943
    model = t_c_Db
=======

    model = t_c_Db
>>>>>>> 3130e815ab317f907f45821185e68001f3c9c9ce
    fields = [
        "question",
    ]
    template_name = 'Update.html'
    success_url = '/'


class DeleteTheView(DeleteView):
    model = t_c_Db
    template_name = 'Delete.html'
    success_url = '/'
    """


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
            return redirect('me')
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
        return redirect('me')
    return render(request, 'sign_up.html')


#############################################
class TermsPoliciesView(ListView):  # list the texts inserted into the database into the html file created here
    model = PrivacyPolicyQuestions
    template_name = 't-c-preview.html'

    def terms_policies(self, request):
        new_user = t_c_Db.objects.all().values()
        args = {'new_user': new_user}
        return render(request, 't-c-preview.html', args)


class NewCreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'create.html'
    success_url = 'list'

class LoggedUser(TemplateView):
    template_name = 'users.html'

    def get(self, request):
        form = forms.UserModelForm()
        return render(request, self.template_name, {'form': form} )

    def post(self, request):
        if request.method == "POST":
            form = forms.UserModelForm(request.POST)
            if form.is_valid():
                form.save()
                reg_date = form.cleaned_data['reg_date']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                contact_no = form.cleaned_data['contact_no']
                company = form.cleaned_data['company']
                user_address = form.cleaned_data['user_address']

            args = {'form': form, 'reg_date': reg_date, 'username': username, 'email': email, 'password': password,
                'contact_no': contact_no, 'company': company, 'user_address': user_address}
        return redirect('/list', args)






def post(self, request):
    get_id = PrivacyPolicyQuestions.objects.get(pk=1)
    if request.method == "POST":
        other_policyUseChoice = request.POST['other_policyUseChoice']
        userLocate = request.POST['userLocate']
        userCreateAccount = request.POST['userCreateAccountl']
        websiteOffer = request.POST['userCreateAccount']
        reg_date = request.POST['reg_date']
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        company = request.POST['company']
        contact_no = request.POST['contact_no']
        user_address = request.POST['user_address']
        age = request.POST['age']
        input_age = request.POST['exact_age']
        containAds = request.POST['containAds']
        upPostContent = request.POST['upPostConten']
        disclosePerInfo = request.POST['disclosePerInfo']
        wsecureMeausre = request.POST['wsecureMeausre']
        country = request.POST['country']

        user = PrivacyPolicyQuestions(registration_date=reg_date, username=username, email=email, password=password,
                         company=company, user_address=user_address, contact_no=contact_no, age=age,
                         input_age=input_age, containAds=containAds, upPostContent=upPostContent,
                                      disclosePerInfo=disclosePerInfo, wsecureMeausre=wsecureMeausre, country=country)

        user.save()
        return redirect('me')
    return render(request, 'users.html', {'get_id': get_id})


def constuction(request):
    value = request.POST['construction']
    return value


def finance(request):
    value = request.POST['finance']
    return value

def health_care(request):
    value = request.POST['health care']
    return value

def real_estate(request):
    value = request.POST['real estate']
    return value

def employment(request):
    value = request.POST['employment']
    return value

def question1(request):
    if request.method == "POST":
        construction = request.POST["browser"]
        if construction == "Construction":
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
        return render(request, 't-c-preview.html', {'user': user})

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


def contact_us(request):
    return render(request, 'contact.html')


def question(request):
    return render(request, 'privacypolicy.html')


def question2(request):
    return render(request, '1collection.html')

