from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'createdAt', 'likeCount',
            'price', 'pricePreview', 'priceType', 'priceUnit',
            'quantity', 'status', 'category', 'specs', 'user',
            'user_id', 'city', 'region'
        ]
        read_only_fields = ['id', 'createdAt', 'likeCount']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        job = Job.objects.create(user=user, **validated_data)
        return job

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            user = User.objects.get(id=user_id)
            instance.user = user
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['priceType'] = instance.get_priceType_display()
        representation['priceUnit'] = instance.get_priceUnit_display()
        representation['status'] = instance.get_status_display()
        return representation