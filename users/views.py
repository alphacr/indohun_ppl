from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SplitUpdateForm
from .models import Profile
from blog.models import Questionnaire, Questionnaire35001

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Akun anda dengan nama {username} sudah dibuat. Anda sekarang dapat masuk ke dalam laman ini')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        s_form = SplitUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and s_form.is_valid():
            u_form.save()
            p_form.save()
            s_form.save()
            messages.success(request, f'Profil Akun anda sudah diperbarui')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        s_form = SplitUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        's_form': s_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_page(request):
    try:
        reports = Questionnaire.objects.filter(author=request.user)
        reports_35001 = Questionnaire35001.objects.filter(author=request.user)
        all_reports = reports.union(reports_35001)
    except:
        reports = None
        reports_35001 = None
        all_reports = None
    context = {
        'posts': Profile.objects.filter(user=request.user),
        'all_reports' : all_reports,
        'report_id': all_reports.order_by('-id')[0],
        'total_count': all_reports.count()
    }
    return render(request, 'users/profile_page.html', context)
