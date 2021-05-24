from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    birth_day = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.birth_day = validated_data.get('birth_day', instance.birth_day)
        instance.save()
        return instance