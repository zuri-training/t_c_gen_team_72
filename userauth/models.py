from unicodedata import category
from django.db import models


class t_c_Db(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
class Terms_and_condition(models.Model):
    category = models.CharField(max_length=50, null=False, unique=False)
    tnc_or_policy = models.CharField(max_length=50, null=False, unique=False)
    body = models.TextField(null=False, blank=False)
    class Meta:
        db_table = "t_C"

        def __str__(self):
            return self.body


# policy generator form - All question fields on UI
class PrivacyPolicyQuestions(models.Model):
    """
    in our route '/question/3' the form field that takes in input the industry type returns a boolean value to the
    fields in this model
    """
    policyUseChoice = (
    ("Web", "Website"),
    ("App", "Mobile Application")
)
    other_policyUseChoice = models.CharField(max_length=50, null=True)
    construction = models.BooleanField(null=True)
    finance = models.BooleanField(null=True)
    employment = models.BooleanField(null=True)
    freelancer = models.BooleanField(null=True)
    health_care = models.BooleanField(null=True)
    saas = models.BooleanField(null=True)
    entertainment = models.BooleanField(null=True)
    real_estate = models.BooleanField(null=True)









