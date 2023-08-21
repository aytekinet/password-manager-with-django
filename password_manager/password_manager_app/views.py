from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'myapp/index.html')

# views.py

from .models import Password

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Password

def dashboard(request):
    passwords = Password.objects.filter(user=request.user)
    paginator = Paginator(passwords, 10)  # 10 parola her sayfada gösterilecek

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'myapp/dashboard.html', {'page': page})

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


from django.shortcuts import render, redirect, get_object_or_404
from .models import Password

def delete_password(request, password_id):
    password = get_object_or_404(Password, pk=password_id)

    if request.method == 'POST':
        password.delete()
        return redirect('dashboard')

    return render(request, 'myapp/delete_password_confirm.html', {'password': password})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Password
from .forms import PasswordForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Password
from .forms import PasswordForm

def update_password(request, password_id):
    password = get_object_or_404(Password, pk=password_id)
    
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            # Mevcut şifrenin verilerini formdan gelen verilerle güncelle
            password.website = form.cleaned_data['website']
            password.username = form.cleaned_data['username']
            new_password = form.cleaned_data['password']
            
            if new_password == form.cleaned_data['confirm_password']:
                password.password = new_password
                password.save()
                return redirect('dashboard')
            else:
                form.add_error('confirm_password', 'Parolalar uyuşmuyor.')
    else:
        form = PasswordForm(initial={
            'website': password.website,
            'username': password.username,
            'password': password.password
        })
    
    return render(request, 'myapp/update_password.html', {'form': form, 'password': password})
