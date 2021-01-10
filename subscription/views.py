from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from djstripe import webhooks

@csrf_exempt
@webhooks.handler("customer.subscription.trial_will_end")
def my_handler(request, **kwargs):
    print(request.body)
    return HttpResponse(status=200)