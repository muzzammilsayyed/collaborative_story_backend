# stories/urls.py
from django.urls import path
from . import views
from .views import StoryListCreate, StoryDetail, AddContribution

urlpatterns = [
    path('', StoryListCreate.as_view(), name='story-list-create'),
    path('<int:pk>/', StoryDetail.as_view(), name='story-detail'),
    path('<int:pk>/contribute/', AddContribution.as_view(), name='add-contribution'),
]



