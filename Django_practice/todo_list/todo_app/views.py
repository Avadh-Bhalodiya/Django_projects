from django.shortcuts import redirect
from .models import TodoListItem
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class LoginToDo(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class SignUpPage(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)  
        return super(SignUpPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SignUpPage, self).get(*args, **kwargs)


class TodoHome(LoginRequiredMixin ,ListView):
    model = TodoListItem
    template_name = 'home.html'
    context_object_name = 'all_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_item'] = context['all_item'].filter(user = self.request.user)
        context['count'] = context['all_item'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['all_item'] = context['all_item'].filter(title__startswith = search_input)
            
        context['search_input'] = search_input

        return context

class TaskDetails(LoginRequiredMixin ,DetailView):
    model = TodoListItem
    template_name = 'details.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin ,CreateView):
    model = TodoListItem
    template_name = 'form.html'
    fields = ['title', 'content', 'complete']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin ,UpdateView):
    model = TodoListItem
    template_name = 'form.html'
    fields = ['title', 'content', 'complete']
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = TodoListItem
    context_object_name = 'all_item'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')