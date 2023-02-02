from rest_framework import serializers
from .models import Man

class ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = Man
        fields = ('title', 'cat_id')