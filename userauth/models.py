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
        ("AD", "Adamawa")
        #Tope is to compile all the state names since he is writing it manually. I no get strength abeg - Lola
    )


    def __str__(self):
        return self.title


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

def decides():
    return month_choice


def new_decides():
    return month_choice1


def newer_decides():
    return month_choice2

class Question(models.Model):
    question_text = models.CharField(max_length=200, choices=decides(), default='JANUARY')
    pub_date = models.DateTimeField('publication_date')
