from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from petstagram.account.forms import LoginForm, RegisterForm, ProfileForm
from petstagram.account.models import PetstagramProfile
from petstagram.pets.models import Pet


def login_user(req):
    if req.POST:
        form = LoginForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('landing page')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(req, 'login.html', context)


def register_user(req):
    if req.POST:
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('landing page')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(req, 'register.html', context)


def logout_user(req):
    logout(req)
    return redirect('landing page')


@login_required
def profile_details(req):
    profile = PetstagramProfile.objects.get(pk=req.user.id)
    if req.POST:
        form = ProfileForm(
            req.POST,
            req.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_pets = Pet.objects.filter(user_id=req.user.id)
    context = {
        'form': form,
        "pets": user_pets,
        'profile': profile,
    }
    return render(req, 'user_profile.html', context)
