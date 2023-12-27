from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('price/', views.price , name="price"),
]