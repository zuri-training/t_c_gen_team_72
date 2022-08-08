from django.db import models


# Create your models here.
class t_c_Db(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserModel(models.Model):
    # the model is equivalent to using sql query  <<Create table UserModel(username varchar(100), email varchar(50), ..)
    registration_date = models.DateTimeField('date published')
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    contactNumber=models.IntegerField(default=23480000000)
    company = models.CharField(max_length=150)
    userAddress=models.CharField(max_length=200)
    businessType =(
        ("CO", "Content Creator"),
        ("BO", "Business Owner"),
        ("EN", "Entrepreneur"),
        ("GB", "Government Body"),
        ("SP", "Software Product")
    )
    state= (
        ("AB", "Abia"),
        ("FC", "Abuja Federal Capital Territory"),
        ("AD", "Adamawa"),
        ("AK", "Akwa Ibom"),
        ("AN", "Anambra"),
        ("BA", "Bauchi"),
        ("BY", "Bayelsa"),
        ("BE", "Benue"),
        ("BO", "Borno"),
        ("CR", "Cross River"),
        ("DE", "Delta"),
        ("EB", "Ebonyi"),
        ("ED", "Edo"),
        ("EK", "Ekiti"),
        ("EN", "Enugu"),
        ("GO", "Gombe"),
        ("IM", "Imo"),
        ("JI", "Jigawa"),
        ("KD", "Kaduna"),
        ("KN", "Kano"),
        ("KT", "Katsina"),
        ("KE", "Kebbi"),
        ("KO", "Kogi"),
        ("KW", "Kwara"),
        ("LA", "Lagos"),
        ("NA", "Nasarawa"),
        ("NI", "Niger"),
        ("OG", "Ogun"),
        ("ON", "Ondo"),
        ("OS", "Osun"),
        ("OY", "Oyo"),
        ("PL", "Plateau"),
        ("RI", "Rivers"),
        ("SO", "Sokoto"),
        ("TA", "Taraba"),
        ("YO", "Yobe"),
        ("ZA", "Zamfara")

        #Tope is to compile all the state names since he is writing it manually. I no get strength abeg - Lola
    )


    def __str__(self):
        return self.title

#policy generator form - All question fields on UI
class privacyPolicyQuestions(models.Model):
    policyUseChoice = (
    ("Web", "Website"),
    ("App", "Mobile Application")  
)
    other_policyUseChoice=models.CharField(max_length=50)
    userLocate =models.BooleanField()
    userCreateAccount=models.BooleanField()
    websiteOffer=models.BooleanField()
    personalInfo=(
        ("NA", "Names"),
        ("Phone No", "Phone Number"),
        ("Email Ad", "Email Address"),
        ("Mail Ad", "Mailing Address"),
        ("Job", "Job Titles"),
        ("User", "Usernames"),
        ("Pass", "Passwords"),
        ("Contact Pref", "Contact Preferences"),
        ("Auth Data", "Authentication Data"),
        ("Bill Ad", "Billing Addresses"),
        ("Cred", "Credit Card Numbers")
    )
    other_personalInfo=models.CharField(max_length=50)
    collectPersonalInfo=models.BooleanField()
    marketingCommnuication=models.BooleanField()
    acceptPayments=models.BooleanField()
    containAds=models.BooleanField()
    upPostContent=models.BooleanField()
    disclosePerInfo=models.BooleanField()
    discloseCollectInfo=models.BooleanField()
    secureMeausre=models.BooleanField()
    planToUse=(
        ("Google", "Google or Web Beacons"),
        ("Apis", "Google Map Apis"),
        ("Both", "Both"),
        ("Neith", "Neither")
    )
    provideService=models.BooleanField()
    provideEmailAdd=models.CharField(max_length=50)
    legalName=models.CharField(max_length=200)
    tradeNameBusiness=models.BooleanField()
    companyEmail=models.CharField(max_length=50)
    phoneNumber=models.IntegerField()
    fax=models.IntegerField()
    country=(
        ("AB", "Abia"),
        ("AD", "Adamawa")
        #Tope is to compile all the state names since he is writing it manually. I no get strength abeg - Lola
    )
    compAddressLine=models.CharField(max_length=200)
    cityTown=models.CharField(max_length=150)
    zipCode=models.IntegerField()
    versionDate=models.DateField()


def decision(self):
    return self.policyUseChoice

def decision(self):
    return self.personalInfo

def decision(self):
    return self.planToUse

def decision(self):
    return self.country


class Question(models.Model):
    pass

#I will continue if this is okay to proceed Ire. Please check.







#month_choice1 = (
    #("JANUARY", "JAN1"),
    #("FEBR", "FEB1"),
    #("MARC", "MAR1"),
    #("APRI", "APR1")
#)
#month_choice2 = (
 #   ("JANUARY", "JAN2"),
  #  ("FEBRUARY", "FEB2"),
   # ("MARCH", "MAR2"),
    #("APRIL", "APR2")
#)

#def decides():
 #   return month_choice


#def new_decides():
 #   return month_choice1


#def newer_decides():
 #   return month_choice2

#class Question(models.Model):
   # question_text = models.CharField(max_length=200, choices=decides(), default='JANUARY')
   # pub_date = models.DateTimeField('publication_date')
