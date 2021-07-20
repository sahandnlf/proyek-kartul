from django.shortcuts import render, redirect

from .models import Task

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy



class LoginViewCustom(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class LogoutView(LogoutView):
    model= Task

class Pendaftaran(FormView):
    template_name= 'base/pendaftaran.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Pendaftaran, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Pendaftaran, self).get(*args, **kwargs)


class ListView(LoginRequiredMixin, ListView):
    template_name= 'base/daftar_aktivitas.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(selesai=False).count()
        
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                judul__startswith=search_input)

        context['search_input'] = search_input

        return context

class CreateView(LoginRequiredMixin, CreateView):
    template_name = 'base/tambah_aktivitas.html'
    model = Task
    fields = ['judul', 'deskripsi']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit_aktivitas.html'
    model = Task
    fields = ['judul', 'deskripsi', 'selesai']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'base/konfirmasi_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')



