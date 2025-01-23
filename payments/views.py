from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework import viewsets,status
from .models import Payment
from .serializers import PaymentSerializer
from paystack_gateway import PaystackGateway
import json
from rest_framework.exceptions import NotFound


# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    
    def get_object(self):
        payment_id = self.kwargs.get('pk')  # 'pk' is the default lookup field in DRF
        try:
            return Payment.objects.get(payment_id=payment_id)
        except Payment.DoesNotExist:
            raise NotFound('Payment not found')
    
    def create(self, request, *args, **kwargs):
        data = request.data
        customer_name = data['customer_name']
        customer_email = data['customer_email']
        amount = data['amount']
        paystack_gateway = PaystackGateway()
        payment_id, authorization_url = paystack_gateway.initiate_payment(customer_name, customer_email, amount)
        
        payment = Payment.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            amount=amount,
            payment_id=payment_id
        )
        return Response({'payment_id': payment_id, 'authorization_url': authorization_url}, status=status.HTTP_201_CREATED)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        paystack_gateway = PaystackGateway()

        try:
            payment_status = paystack_gateway.retrieve_payment_status(instance.payment_id)
            print(f"Retrieved Payment Status: {payment_status}")  # Log the status
            instance.status = payment_status
            instance.save()  # Update the database
            print(f"Updated Database Status: {instance.status}")  # Confirm database update

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'Failed to retrieve payment status', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




