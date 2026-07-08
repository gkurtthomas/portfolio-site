from django.contrib import admin

# Register your models here.
from .models import PersonalInformation, Project

admin.site.register(PersonalInformation)
admin.site.register(Project)