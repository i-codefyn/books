from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.generic.base import TemplateView


razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class OrdersPageView(TemplateView):
   template_name = 'orders/purchase.html'



   def get_context_data(self, **kwargs): # new
     context = super().get_context_data(**kwargs)
     context['razorpay_key'] = settings.RAZORPAY_KEY_ID
     return context

def charge(request): # new
    permission = Permission.objects.get(codename='special_status')
    u = request.user
    u.user_permissions.add(permission)

    if request.method == 'POST':
       charge = razorpay.Charge.create(
       amount=3900,
       currency='usd',
       description='Purchase all books',
       source=request.POST['razorpayToken']
)
    return render(request, 'orders/charge.html')
