from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        address = request.POST['address']



        #send a mail
        send_mail(
        'ORDER '+ 'confirmed ' + name, #SUBEJECT
        '\n\nYour Order is :\n' +message + '\n\nDelivering To :\n ' +address + '\n\nYour Phone No. : \n' +phone, #message 
        email, #from email
        ['warehouse.homecooks.server@gmail.com' , email ] #to email
        )  

        return render(request, 'home.html', {'name' : name}) #we can add thankyou page here and i can add name too
    
    else:
        return render(request, 'home.html', {})


def butterpaneer(request):
    return render(request, 'butterpaneer.html', {})
