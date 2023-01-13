from django.urls import path

from todo.views import TodoDetail, TodoList

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
]
