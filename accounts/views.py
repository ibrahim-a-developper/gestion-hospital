from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout

from .models import Profile




# Create your views here.


# @unauthenticated_user

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation utilisateur bien ajoute")

            return redirect('accounts:signup')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')




def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('personne:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)
