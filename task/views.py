from typing_extensions import Self
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
import stripe
from django.conf import settings
from django.urls import reverse
from . import models
from .models import price


def index(request): 


    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    
    
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
    'name': 'The Global NFT Summit London 2022',
    'amount': models.price()*100,
    'currency': 'gbp',
    'quantity': 1,
    }],
    
    payment_intent_data={
    'application_fee_amount': models.price()*10,
    'transfer_data': {
      'destination': 'acct_1LNEQOB6Nyoxs5i0',
    },
    },

    mode='payment',
    success_url='https://example.com/success',
    cancel_url='https://example.com/failure'
)
    


    context={
        'session_id':session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'px': models

    }
    return render(request,'task/index.html',context)