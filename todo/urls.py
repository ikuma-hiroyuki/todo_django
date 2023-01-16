from django.urls import path

from todo.views import TodoCreate, TodoDelete, TodoDetail, TodoList, TodoUpdate

urlpatterns = [
    path('', TodoList.as_view(), name='list'),  # reverse_lazy('list')で指定
    path('list/', TodoList.as_view(), name='list'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
]
