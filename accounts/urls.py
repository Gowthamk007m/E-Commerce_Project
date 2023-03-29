from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.register_view,name='sign_up'),
    path('logout',views.logout,name='logout')

]
