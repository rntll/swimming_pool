from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm, InfoForm, CommentForm, ReviewForm
from .models import UserProfile, Comment, Review, Info
from .decorators import user_required, superuser_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Создаем профиль пользователя
            profile = UserProfile.objects.create(user=user)

            # Создаем форму InfoForm и связываем ее с профилем пользователя
            info_form = InfoForm(request.POST, instance=profile)
            if info_form.is_valid():
                info_form.save()

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@superuser_required
def admin_panel_view(request):
    #Исключаем суперпользователей из выборки
   user_profiles = UserProfile.objects.filter(is_superuser=False)

    #Передаем данные в контекст шаблона
   context = {
       'user_profiles': user_profiles,
   }

    #Отображаем шаблон с переданными данными
   return render(request, 'accounts/admin_panel.html', context)



def profile_view(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('accounts:admin_panel'))
    elif request.user.username:
        return HttpResponseRedirect(reverse('accounts:profile'))
    user_profile = UserProfile.objects.get(user=request.user)
    info = Info.objects.get(user_profile=user_profile)
    context = {
        'user_profile': user_profile,
        'info': info
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def add_info(request):
    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        if info_form.is_valid():
            info = info_form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            info.user_profile = user_profile
            info.save()
            return redirect('accounts:profile')
    else:
        info_form = InfoForm()
    return render(request, 'accounts/add_info.html', {'info_form': info_form})


def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            review.user = user_profile
            review.save()
            return redirect('accounts:review_page')
    else:
        form = ReviewForm()
    return render(request, 'accounts/review_page.html', {'form': form})
@login_required
def add_comment(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('review_page')
    else:
        form = CommentForm()
    return render(request, 'accounts/add_comment.html', {'form': form, 'review': review})