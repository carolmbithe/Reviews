from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Project
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewProjectForm,NewProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects=Project.get_projects()
    return render(request,'index.html',{"projects":projects})

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def profile(request):
    current_user=request.user
    projects=Project.objects.filter(profile=current_user).all()
    profile = Profile.objects.filter(user=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(user=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

def edit_profile(request):
    current_user=request.user
    # profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'edit_profile.html',{"form":form})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
