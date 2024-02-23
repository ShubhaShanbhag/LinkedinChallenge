from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfo
from .forms import SignupForm, UserProfileForm

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            jobtitle = form.cleaned_data['jobtitle']

            user_profile, created = UserInfo.objects.get_or_create(
                user=user)
            user_profile.jobtitle = jobtitle
            user_profile.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def index(request):
    members = UserInfo.objects.all()
    print(members)
    return render(request, 'core/index.html', {
        'members': members,
    })


def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def profileUser(request):
    user_profile, created = UserInfo.objects.get_or_create(
        user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()

    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'core/profile.html', {'user_profile': user_profile, 'profile_form': profile_form})


@login_required
def profile(request, user_id):
    user_profile = get_object_or_404(UserInfo, user__id=user_id)
    return render(request, 'core/profile.html', {'user_profile': user_profile}) 

