from django.contrib import admin

from .models import PrivacyPolicyQuestions

admin.site.register(PrivacyPolicyQuestions)

from .models import *


# Register your models here.
admin.site.register(Terms_and_condition)