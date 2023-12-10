from .models import QA,Interview
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = "__all__"