# apis/serializers.py

from rest_framework import serializers
from .models import User  # Đảm bảo import đúng model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['m_id', 'm_user_name', 'm_password']  # Các trường bạn muốn hiển thị trong API