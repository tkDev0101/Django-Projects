from django.shortcuts import get_object_or_404, redirect
from .models import QRCode
from django.shortcuts import render
from django.http import HttpResponse              
from django.shortcuts import render, get_object_or_404


                       
def index(request):                                                     
    return HttpResponse("Hello, World!")  



def qr_redirect_view(request, code):
    qr = get_object_or_404(QRCode, code=code, is_active=True)
    qr.scan_count += 1
    qr.save()
    return redirect(qr.target_url)




def qr_detail_view(request, code):
    qr = get_object_or_404(QRCode, code=code)
    return render(request, 'qrapp/qr_detail.html', {'qr': qr})

