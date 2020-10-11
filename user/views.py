# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import SignUpForm

def home(request):
    return render(request, 'home_basic.html')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})