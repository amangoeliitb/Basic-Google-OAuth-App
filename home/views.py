from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


@login_required
def Home(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'home/home.html', {
        'profile': profile
    })
