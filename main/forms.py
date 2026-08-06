from django import forms

from .models import (
    Project,
    Inquiry,
    Testimony,
)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "project_name",
            "description",
            "tech_stack",
            "link",
        ]

class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry

        fields = "__all__"

class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony

        fields = "__all__"