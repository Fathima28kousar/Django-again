from django.shortcuts import render
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email') 
        amount = int(request.POST.get('amount')) * 100
        
        # Initializing Razorpay client
        client = razorpay.Client(auth=('rzp_test_wucadtaz2NQLqm', 'Un2BvQcbNWU4MpjvhlF28G9W'))
        
        # Creating the payment order
        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'  # Automatically captures the payment
        })
        
        order_id = payment['id']
        order_status = payment['status']

        if order_status == 'created':
            coffee = Coffee(
                name = name,
                amount = amount,
                order_id = order_id,
            )
            coffee.save()
            payment['name'] = name
        # Rendering the template with payment details
        return render(request, 'index.html', {'payment': payment})
    
    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        client = razorpay.Client(auth=('rzp_test_wucadtaz2NQLqm', 'Un2BvQcbNWU4MpjvhlF28G9W'))
        
        try:
            # Retrieving parameters from the request
            razorpay_order_id = a.get('razorpay_order_id')
            razorpay_payment_id = a.get('razorpay_payment_id')
            razorpay_signature = a.get('razorpay_signature')
            
            # Verifying payment signature
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            status = client.utility.verify_payment_signature(params_dict)
            
            # Updating payment status in the database
            coffee = Coffee.objects.filter(order_id=razorpay_order_id).first()
            if coffee:
                coffee.razorpay_payment_id = razorpay_payment_id
                coffee.paid = True
                coffee.save()
                
            return render(request, 'success.html', {'status': True})
        
        except Exception as e:
            print(str(e))  # error for debugging purposes
            return render(request, 'success.html', {'status': False})
        
    return render(request, 'success.html')
