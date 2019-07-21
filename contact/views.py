from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models

# Create your views here.
def contact(request):
    return render(request,'contact/contact.html',{})


def contact_backend(request):
    v1  = request.POST['Fname']
    v2  = request.POST['Lname']
    v3  = request.POST['Email']
    v4  = request.POST['Massege']
    new = models.contact(Fname = v1, Lname = v2, Email = v3, Massege = v4)
    new.save()
    return render(request,'contact/done.html',{})