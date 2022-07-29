from django.urls import path
from .views import registerUser, logoutUser, loginUser



urlpatterns = [
    path('register-user', registerUser , name='register-user'),
    path('logout', logoutUser, name='logout'),
    path('login/', loginUser, name='login'),
]