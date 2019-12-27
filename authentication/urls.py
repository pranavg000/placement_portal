from django.urls import path
from authentication import views
from home import views as home_views

app_name = 'authentication'
urlpatterns = [
    # The home view ('/authentication/')
    path('', views.home, name='home'),
    # Explicit home ('/authentication/home/')
    path('home/', views.home, name='home'),
    # Redirect to get token ('/authentication/gettoken/')
    path('authentication/gettoken/', views.gettoken, name='gettoken'),

    path('authentication/gettoken/success/', views.success, name='success'),
]
