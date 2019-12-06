from rest_framework import serializers
from .models import Animal, Capture

class AnimalSerializer(serializers.ModelSerializer):
    captures = serializers.HyperlinkedIdentityField(view_name='capture-detail',many=True, read_only=True)
    class Meta:
        model=Animal
        fields = ['tag','captures']

class CaptureSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    class Meta:
        model = Capture
        fields = ['photo','animal','newCap']

    def create(self, validated_data):
        newCap = validated_data.pop('newCap')
        animal_data = validated_data.pop('animal')
        if newCap:
            animal = Animal.objects.create(**animal_data)
        else:
            print(animal_data)
            animal = Animal.objects.get(**animal_data)
        capture = Capture.objects.create(animal=animal,**validated_data)
        return capture