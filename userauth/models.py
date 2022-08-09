from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class t_c_Db(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

"""
class UserModel(models.Model):
    # the model is equivalent to using sql query  <<Create table UserModel(username varchar(100), email varchar(50), ..)
    registration_date = models.DateTimeField('date published')
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    contactNumber=models.IntegerField(default=23480000000)
    company = models.CharField(max_length=150)
    userAddress = models.CharField(max_length=200)
#    input_age = models.IntegerField()
#    age = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    businessType =(
        ("CO", "Content Creator"),
        ("BO", "Business Owner"),
        ("EN", "Entrepreneur"),
        ("GB", "Government Body"),
        ("SP", "Software Product")
    )
    state= (
        ("AB", "Abia"),
        ("AD", "Adamawa")
        #Tope is to compile all the state names since he is writing it manually. I no get strength abeg - Lola
    )

    def __str__(self):
        return self.username, self.email


month_choice = (
    ("JANUARY", "JAN"),
    ("FEBRUARY", "FEB"),
    ("MARCH", "MAR"),
    ("APRIL", "APR")
)
month_choice1 = (
    ("JANUARY", "JAN1"),
    ("FEBR", "FEB1"),
    ("MARC", "MAR1"),
    ("APRI", "APR1")
)
month_choice2 = (
    ("JANUARY", "JAN2"),
    ("FEBRUARY", "FEB2"),
    ("MARCH", "MAR2"),
    ("APRIL", "APR2")
)
"""

class PrivacyPolicyQuestions(models.Model):
    other_policyUseChoice = models.CharField(max_length=50, null=True)
    userLocate = models.BooleanField(null=True)
    userCreateAccount = models.BooleanField(null=True)
    websiteOffer = models.BooleanField(null=True)
    other_personalInfo = models.CharField(max_length=50, null=True)
    collectPersonalInfo = models.BooleanField(null=True)
    marketingCommnuication = models.BooleanField(null=True)
    acceptPayments = models.BooleanField(null=True)
    containAds = models.BooleanField(null=True)
    upPostContent = models.BooleanField(null=True)
    disclosePerInfo = models.BooleanField(null=True)
    discloseCollectInfo = models.BooleanField(null=True)
    secureMeausre = models.BooleanField(null=True)
    planToUse=(
        ("Google", "Google or Web Beacons"),
        ("Apis", "Google Map Apis"),
        ("Both", "Both"),
        ("Neith", "Neither")
    )
    provideService = models.BooleanField(null=True)
    provideEmailAdd = models.CharField(max_length=50, null=True)
    legalName = models.CharField(max_length=200, null=True)
    tradeNameBusiness = models.BooleanField(null=True)
    companyEmail = models.CharField(max_length=50, null=True)
    phoneNumber = models.IntegerField(null=True)
    fax = models.IntegerField(null=True)
    compAddressLine = models.CharField(max_length=200, null=True)
    cityTown = models.CharField(max_length=150, null=True)
    zipCode = models.IntegerField(null=True)
    versionDate = models.DateField(null=True)

"""
def decides():
    return month_choice


def new_decides():
    return month_choice1


def newer_decides():
    return month_choice2
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200, default='JANUARY')
    pub_date = models.DateTimeField('publication_date')


class Questions(models.Model):
    question = models.CharField(max_length=100)


class TC(models.CharField):
    t_c_text = models.TextField()


