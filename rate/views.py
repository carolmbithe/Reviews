from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Project
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    projects=Project.objects.all()
    return render(request,'index.html',{"projects":projects})
