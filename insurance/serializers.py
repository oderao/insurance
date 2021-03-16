
from rest_framework import serializers

from .models import RiskName,RiskDetails

class RiskNameSerializer(serializers.HyperlinkedModelSerializer):
	
    class Meta:
        model = RiskName
        fields = ('id', 'name')

class RiskDetailsSerializer(serializers.HyperlinkedModelSerializer):
	
    class Meta:
        model = RiskDetails
        fields = ('risk_id','risk_name','risk_duration','risk_amount','risk_active_date')
