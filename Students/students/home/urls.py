from django.urls import include, path
from .views import StudentsView

urlpatterns = [
    path('', StudentsView.as_view(
        {'get': 'list', 'post': 'create'}), name='students_list'),
]
