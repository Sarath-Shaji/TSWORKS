from rest_framework import serializers
from apple.models import Apple

class AppleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apple
        fields=('date','open','high','low','close','adjclose','volume')