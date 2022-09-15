from django.shortcuts import render

from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
...
# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)
data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Fathan Hadyan'
}

def XML_wishlist(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def JSON_wishlist(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def JSON_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)   
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  

def XML_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id) 
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")