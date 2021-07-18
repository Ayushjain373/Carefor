from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  .models import Donation
import razorpay

def home(request):
   if request.method =="POST":

      
      name = request.POST["name"]
      amount = request.POST["amount"]
      
      client = razorpay.Client(auth = ("rzp_test_LR2V7TWcpMUYUm", "ZuDG1JOVy3zUKSz2zCpxUIlV"))
      order_amount = int(amount)*100
    
      payment = client.order.create({'amount':order_amount, 'currency': 'INR', 'payment_capture':'1'})

      donation = Donation(name = name , amount = amount , payment_id = payment['id'])
      donation.save()
     
   context={

      "pay" : payment
   }
   # params={'payment': payment}
   res=render(request,'home/index.html',context)
   return res

def success(request):
   res = render(request,'home/success.html')
   return res

# Create your views here.

