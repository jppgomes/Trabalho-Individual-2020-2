"""
api URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import TaskCreate, TaskList, TaskDetail, TaskUpdate, TaskDelete

urlpatterns = [
    path('create/', TaskCreate.as_view(), name='create-task'),
    path('', TaskList.as_view()),
    path('<int:pk>/', TaskDetail.as_view(), name='retrieve-task'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete-task')
]
