from django import forms

from .models import (
    Project,
    Inquiry,
    Testimony,
)

def add_bootstrap_classes(form):
    for field in form.fields.values():
        field.widget.attrs.update({
            "class": "form-control"
        })
        
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "project_name",
            "description",
            "tech_stack",
            "link",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_bootstrap_classes(self)

class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry

        fields = "__all__"


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        add_bootstrap_classes(self)

class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony

        fields = "__all__"


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        add_bootstrap_classes(self)