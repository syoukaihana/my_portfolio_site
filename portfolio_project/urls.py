from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),  # galleryアプリのURLを追加
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ログインURLを追加
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # ログアウトURLを追加
]

# 開発環境でメディアファイルを提供する
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
