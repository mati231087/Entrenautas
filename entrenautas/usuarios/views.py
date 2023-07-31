from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # mensaje de error
            pass
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
# Create your views here.
