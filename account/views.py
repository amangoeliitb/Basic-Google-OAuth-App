from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from home.models import Profile


def Register(strategy, details, user=None,
             is_new=False, image=None, *args, **kwargs):
    if(is_new):
        user.save()
        profile = Profile()
        profile.user = user
        profile.save()
    else:
        return


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
