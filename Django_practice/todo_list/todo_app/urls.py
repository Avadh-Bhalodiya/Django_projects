from django.urls import path
from .views import TodoHome, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, LoginToDo, SignUpPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginToDo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('home/', TodoHome.as_view(), name = 'home'),
    path('task-detail/<int:pk>/', TaskDetails.as_view(), name='task-detail'),
    path('create-task/', TaskCreate.as_view(), name = 'create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
]