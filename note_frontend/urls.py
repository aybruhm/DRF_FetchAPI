from django.urls import path
from .views import home, create_thought, update_thought, \
    delete_thought, login, register, profile

app_name = "note"

urlpatterns = [
    path('', home, name="home"),
    path('new-thought/', create_thought, name="new-thought"),
    path('update-thought/<int:pk>/', update_thought, name="update-thought"),
    path('delete-thought/<int:pk>/', delete_thought, name="delete-thought"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
]
