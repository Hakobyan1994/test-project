from rest_framework import serializers
from ..models import PersonDate


class PersonDateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PersonDate
        fields = ['id', 'first_name', 'last_name', 'city','country','index']
        read_only_fields = ['id']



