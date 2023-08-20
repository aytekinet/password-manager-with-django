from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'myapp/index.html')

# views.py

from .models import Password

def dashboard(request):
    passwords = Password.objects.filter(user=request.user)
    return render(request, 'myapp/dashboard.html', {'passwords': passwords})

def login_view(request):
    # Giriş yapma işlemleri burada gerçekleştirilir
    return render(request, 'myapp/login.html')  # Giriş sayfası şablonunu döndürün

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı otomatik olarak giriş yapın
            return redirect('dashboard')  # Kayıt başarılı olduğunda yönlendirilecek sayfa
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def logout_view(request):
    logout(request)  # Oturumu kapat
    return redirect('index')  # Çıkış yaptıktan sonra ana sayfaya yönlendir


# views.py

from django.shortcuts import render, redirect
from .forms import PasswordForm
from .models import Password

def add_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data['website']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                password_obj = Password(user=request.user, website=website, username=username, password=password)
                password_obj.save()
                return redirect('dashboard')
            else:
                error_message = "Parolalar eşleşmiyor."
        else:
            error_message = "Form geçersiz."

    else:
        form = PasswordForm()
        error_message = ""

    return render(request, 'myapp/add_password.html', {'form': form, 'error_message': error_message})
