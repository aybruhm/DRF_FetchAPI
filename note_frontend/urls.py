from django.urls import path
from .views import home, create_thought, update_thought, \
    delete_thought, login_page, register_page, profile_page

app_name = "note"

urlpatterns = [
    path('', home, name="home"),
    path('new-thought/', create_thought, name="new-thought"),
    path('update-thought/<int:pk>/', update_thought, name="update-thought"),
    path('delete-thought/<int:pk>/', delete_thought, name="delete-thought"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('profile/', profile_page, name="profile"),
]
