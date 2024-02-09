from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import book


# Create your views here.
def home(request):
        return render(request,'index.html')

def car(request):
    message = None
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cname = request.POST.get('cname')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        obj = book(Firstname=fname,Lastname=lname,Carname=cname,City=city,State=state,Zip=zip)
        obj.save()
        message = 'Car Booking successfully'
    return render(request,'booking.html',{'message':message})

def show(request, pk= None):
    message = None
    message1 = None
    if pk is not None:
        try:
            obj = book.objects.get(Carname=pk)
            obj.delete()
            message1 = 'User data deleted successfully'
        except:
            message1 = 'No user Found'
    if request.method == 'POST':
        if 'save' in request.POST:
            id = request.POST.get('id')
            fname = request.POST.get('Firstname')
            lname = request.POST.get('Lastname')
            cname = request.POST.get('Carname')
            city = request.POST.get('City')
            obj = book.objects.get(id=id)
            obj.Firstname = fname
            obj.Lastname = lname
            obj.Carname = cname
            obj.City = city
            obj.save()
            message = 'Data updated successfully'
    obj = book.objects.all()
    return render(request,'showbook.html',{'mydata':obj,'message': message,'message1': message1})


