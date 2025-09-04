from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','author']
        extra_kwargs = {"author":{'read_only': True}}
        

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["account_id", "introducer", "beneficiary", "created_by", "created_at"]
        read_only_fields = ["account_id", "beneficiary", "created_by", "created_at"]


