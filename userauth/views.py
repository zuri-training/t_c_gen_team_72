from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import t_c_Db
from django.http import HttpResponse

from . import forms


def testView(request):
    return render(request, "editprofile.html")
def logintest(request):
    return render(request, "loginform.html")




class CreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'home.html'
    success_url = 'list'


class ListTheView(ListView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    template_name = 'listView.html'


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
