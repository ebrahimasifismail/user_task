from django.urls import include, path
from collections import OrderedDict, namedtuple
from django.contrib.auth import views as auth_views
from . import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/', views.user_list, name='users_list'),
    path('signup/', views.signup, name='signup'),
    path('user/<int:pk>/', views.user_detail, name='users_detail'),
]
