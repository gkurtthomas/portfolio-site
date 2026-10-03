from django.contrib import admin

# Register your models here.
from .models import (
    Project,
    PersonalInformation,
    Inquiry,
    Testimony,
    TechStack,
)

admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(Inquiry)
admin.site.register(Testimony)
admin.site.register(TechStack)