from rest_framework import serializers
from .models import *

class lecturerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'
