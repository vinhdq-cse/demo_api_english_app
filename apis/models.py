from django.db import models

class User(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_user_name = models.CharField(max_length=150, unique=True)
    m_password = models.CharField(max_length=128)

    def __str__(self):
        return self.m_user_name