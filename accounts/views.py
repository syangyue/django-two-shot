from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = User.objects.create(
                username=username,
                password=password
            )
            user.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()
    context = {
            'form': form,
         }
    return render(request, "registration/signup.html", context)
