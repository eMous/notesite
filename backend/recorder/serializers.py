from rest_framework import serializers
from .models.core import RecordedUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedUser
        fields = ("id","username","email","first_name","is_staff",)
