from rest_framework import  serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        # fields = ['customer_name','customer_email','amount', 'status']
        fields = '__all__'

    