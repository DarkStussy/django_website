from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from accounts.forms import UserRegistrationForm, UserForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


@login_required
def profile(request):
    if request.method == "POST":
        pass_form = PasswordChangeForm(user=request.user, data=request.POST)
        user_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Your password has been changed successfully!')
        elif user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been saved successfully!')
        elif p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile image has been saved successfully!')
        else:
            messages.error(request, 'Unable to complete request')
        return redirect("profile")
    user_form = UserForm(instance=request.user)
    pass_form = PasswordChangeForm(user=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request=request, template_name="accounts/profile.html", context={"user": request.user,
                                                                                   "user_form": user_form,
                                                                                   "pass_form": pass_form,
                                                                                   "p_form": p_form})
