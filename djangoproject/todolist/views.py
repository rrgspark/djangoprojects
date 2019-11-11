from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import Item

def main(request):
    if request.user.is_authenticated:
        items = Item.objects.all()
        return render(request,'main.html', {'items':items})
    return render(request,'main.html')
