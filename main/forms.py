from django import forms

from .models import (
    Project,
    Inquiry,
    Testimony,
    TechStack,
)

def add_bootstrap_classes(form):
    for field in form.fields.values():
        if isinstance(field.widget, forms.RadioSelect):
            field.widget.attrs.update({
                "class": "form-check-input"
            })
        elif isinstance(field.widget, forms.CheckboxSelectMultiple):
            field.widget.attrs.update({
                "class": "form-check-input"
            })
        else:
            field.widget.attrs.update({
                "class": "form-control"
            })
        
class ProjectForm(forms.ModelForm):
    tech_stack = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
        required=True,
    )

    class Meta:
        model = Project
        fields = [
            "project_name",
            "description",
            "tech_stack",
            "link",
        ]
        labels = {
            "project_name": "Project Name",
            "description": "Project Description",
            "tech_stack": "Tech Stack",
            "link": "Link",
        }
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["link"].required = True

        add_bootstrap_classes(self)

    def save(self, commit=True):
        project = super().save(commit=False)

        if commit:
            project.save()
            project.tech_stack.set([self.cleaned_data["tech_stack"]])

        return project

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

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ["name"]
        labels = {
            "name": "Tech Stack Name",
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if TechStack.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(
                "This tech stack already exists."
            )

        return name