import json

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from order.models import Order
import requests
# Create your views here.


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order , id = order_id)
    tooman_price = order.get_total_sum()
    rial_price = tooman_price * 10
    zarinpal_request = "https://api.zarinpal.com/pg/v4/payment/request.json"
    request_data = {
        'merchant_id': 'aaabbbaaabbbaaabbb',
        'amount': tooman_price,
        'description': f'{order.id} : {order.first_name} : {order.last_name}',
        'callback_url':'https://127.0.0.1:8000',
    }

    request_header = {
        'accept':'application/json',
        'content-type':'application/json',
    }

    res = requests.post(url = zarinpal_request , data  = json.dumps(request_data) , headers = request_header)
    data = res.json()['data']
    authority = data['Authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in  data or len(data)==0:
         return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))


    else:

        return HttpResponse('پرداخت انجام نشد.')





def payment_callback(request):
    authority_payment = request.GET.get('Authority')
    status_payment = request.GET.get('Status')
    order = get_object_or_404(Order , authority_payment = authority_payment)
    tooman_price = order.get_total_sum()
    rial_price = tooman_price * 10

    if status_payment == 'OK':
        request_header = {
            'accept': 'application/json',
             'content-type':'application/json',
        }

        request_data = {
            'merchant_id' : 'aaabbbaaabbbaaabbb',
            'amount':tooman_price,
            'authority':authority_payment,
        }


        res = requests.post(url = "https://api.zarinpal.com/pg/v4/payment/verify.json" , data = json.dumps(request_data) , headers = request_header )
        if 'data' in res.json() and ('errors' not in data or len(data['errors'])==0):
            code = data['code']
            if code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()


                return HttpResponse('پرداخت شما با موفقست انجام شد.')


            elif code == 101:

                return HttpResponse('پرداخت با موفقست انجام شد . البته این تراکنش قبلا هم تکرار شذه بود')


            else:
                return  HttpResponse('تراکنش ناموفق بود .')







