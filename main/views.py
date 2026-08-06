from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalInformation, Project
from .forms import ProjectForm

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