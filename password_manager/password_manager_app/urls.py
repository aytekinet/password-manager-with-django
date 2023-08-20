from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  # veya uygulama adınıza göre: from myapp import views

urlpatterns = [
    # Diğer URL tanımları buraya gelebilir
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Örnek bir dashboard URL tanımı
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),  # 'your_register_view' yerine 'views.register_view' kullanılır
    path('add_password/', views.add_password, name='add_password'),
    path('delete_password/<int:password_id>/', views.delete_password, name='delete_password'),



    # Diğer URL tanımları buraya gelebilir
]
