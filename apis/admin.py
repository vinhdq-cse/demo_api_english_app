from django.contrib import admin
from .models import User

# Đăng ký model User với trang admin
admin.site.register(User)
