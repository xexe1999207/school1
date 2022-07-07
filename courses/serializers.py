from rest_framework.validators import UniqueTogetherValidator
from courses.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']
