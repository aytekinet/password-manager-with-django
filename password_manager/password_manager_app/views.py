from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'myapp/index.html')

def dashboard(request):
    # Dashboard ile ilgili işlemleri burada gerçekleştirin
    return render(request, 'myapp/dashboard.html')  # Dashboard şablonunu döndürün

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
