from django.urls import path
from .views import LoginViewCustom, LogoutView, Pendaftaran, ListView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Pendaftaran.as_view(), name='register'),
    path('', ListView.as_view(), name='tasks'),
    path('task-create/', CreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]