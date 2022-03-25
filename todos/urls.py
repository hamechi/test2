from django.urls import path
from todos.views import TodoDetailAPIView, TodosAPIView

urlpatterns = [
    path('', TodosAPIView.as_view(), name='todos'),
    path('<int:id>/', TodoDetailAPIView.as_view(), name='todo'),
]
