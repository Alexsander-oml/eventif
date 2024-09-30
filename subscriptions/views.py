from django.http import HttpResponse
from django.shortcuts import render
from subscription.forms import SubscriptionForm
# Create your views here.

def subscribe(request):
    return render(request, 'subscriptions/subscription_form.html')