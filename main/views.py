from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalInformation, Project, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm

# Create your views here.
def home(request):
    personal = PersonalInformation.objects.first()
    projects = Project.objects.all()
    
    return render(
        request,
        "main/index.html",
        {
            "personal": personal,
            "projects": projects,
        }
    )

def project_list(request):

    projects = Project.objects.all()

    return render(
        request,
        "main/project_list.html",
        {
            "projects": projects,
        }
    )

def project_detail(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    return render(
        request,
        "main/project_detail.html",
        {
            "project": project,
        }
    )

def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("project_list")

    else:

        form = ProjectForm()

    return render(
        request,
        "main/add_project.html",
        {"form": form},
    )

def add_inquiry(request):

    if request.method == "POST":

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = InquiryForm()

    return render(
        request,
        "main/add_inquiry.html",
        {"form": form},
    )

def add_testimony(request):

    if request.method == "POST":

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = TestimonyForm()

    return render(
        request,
        "main/add_testimony.html",
        {"form": form},
    )