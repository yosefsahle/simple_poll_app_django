from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Poll, Question, Choice, Vote

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'phone', 'gender', 'age', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'created_at']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'question_text']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'choice', 'voted_at']
