from django.urls import path
from .api_views import (
    RegisterView, UserDetailView, PollCreateAPIView, PollListAPIView, PollDetailAPIView, PollUpdateAPIView, PollDeleteAPIView,
    QuestionCreateAPIView, QuestionListAPIView, QuestionDetailAPIView, QuestionUpdateAPIView, QuestionDeleteAPIView,
    ChoiceCreateAPIView, ChoiceListAPIView, ChoiceDetailAPIView, ChoiceUpdateAPIView, ChoiceDeleteAPIView,
    VoteCreateAPIView, VoteListAPIView, VoteDetailAPIView, VoteUpdateAPIView, VoteDeleteAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # User URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Poll URLs
    path('polls/create/', PollCreateAPIView.as_view(), name='poll-create'),
    path('polls/', PollListAPIView.as_view(), name='poll-list'),
    path('polls/<int:id>/', PollDetailAPIView.as_view(), name='poll-detail'),
    path('polls/update/<int:id>/', PollUpdateAPIView.as_view(), name='poll-update'),
    path('polls/delete/<int:id>/', PollDeleteAPIView.as_view(), name='poll-delete'),

    # Question URLs
    path('questions/create/', QuestionCreateAPIView.as_view(), name='question-create'),
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('questions/<int:id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('questions/update/<int:id>/', QuestionUpdateAPIView.as_view(), name='question-update'),
    path('questions/delete/<int:id>/', QuestionDeleteAPIView.as_view(), name='question-delete'),

    # Choice URLs
    path('choices/create/', ChoiceCreateAPIView.as_view(), name='choice-create'),
    path('choices/', ChoiceListAPIView.as_view(), name='choice-list'),
    path('choices/<int:id>/', ChoiceDetailAPIView.as_view(), name='choice-detail'),
    path('choices/update/<int:id>/', ChoiceUpdateAPIView.as_view(), name='choice-update'),
    path('choices/delete/<int:id>/', ChoiceDeleteAPIView.as_view(), name='choice-delete'),

    # Vote URLs
    path('votes/create/', VoteCreateAPIView.as_view(), name='vote-create'),
    path('votes/', VoteListAPIView.as_view(), name='vote-list'),
    path('votes/<int:id>/', VoteDetailAPIView.as_view(), name='vote-detail'),
    path('votes/update/<int:id>/', VoteUpdateAPIView.as_view(), name='vote-update'),
    path('votes/delete/<int:id>/', VoteDeleteAPIView.as_view(), name='vote-delete'),
]
