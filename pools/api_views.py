from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Poll, Question, Choice, Vote
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PollCreateAPIView(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]

class PollListAPIView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetailAPIView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'id'

class PollUpdateAPIView(generics.UpdateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]

class PollDeleteAPIView(generics.DestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChoiceCreateAPIView(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChoiceListAPIView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = 'id'

class ChoiceUpdateAPIView(generics.UpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChoiceDeleteAPIView(generics.DestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteCreateAPIView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteListAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = 'id'

class VoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteDeleteAPIView(generics.DestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]
