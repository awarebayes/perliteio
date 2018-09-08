from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        age = serializers.ReadOnlyField(default=-1)
        prize = serializers.ReadOnlyField(default=-1)
        fields = ('url', 'id', 'created', 'name', 'born', 'age', 'prize')

    def create(self, validated_data):
        del validated_data['owner']
        validated_data['age'] = -1
        validated_data['prize'] = -1
        return Ticket.objects.create(**validated_data)

