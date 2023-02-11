from django.shortcuts import render
from .models import tasks
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
# Create your views here.
class pplloginview(LoginView):
    model= User
    fields='__all__'
    template_name='index.html'
    redirect_authenticated_user = True

    def  get_success_url(self):
        return reverse_lazy('taskviews')
    
class taskviews(ListView, LoginRequiredMixin):
    model=tasks
    context_object_name='tasks'
    template_name='loginsuccess.html'

class taskcreate(CreateView, LoginRequiredMixin):
    model=tasks
    fields=['tilte','description']
    template_name='createtask.html'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    success_url= reverse_lazy('taskviews')

class taskedit(UpdateView, LoginRequiredMixin):
    model=tasks
    context_object_name='task'
    fields=['tilte', 'description']
    template_name='edittask.html'
    # def get_context_data(self, **kwargs):
    #     cont=super().get_context_data('task')
    #     cont['task'] = cont['task'].filter(user=self.request.user)
    success_url= reverse_lazy('taskviews')

class taskdelete(DeleteView, LoginRequiredMixin):
    model=tasks
    template_name='delconfirm.html'
    context_object_name='task'
    success_url= reverse_lazy('taskviews')
