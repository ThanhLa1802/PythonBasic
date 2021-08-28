from django.db import models
from rest_framework import serializers
from .models import Course
class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title','price']