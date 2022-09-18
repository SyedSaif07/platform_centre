from rest_framework import serializers
from activity.models import Activity
from django.contrib.auth.models import User

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'activity']
