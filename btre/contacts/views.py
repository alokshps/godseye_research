from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST': 
         
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                          message=message)

        contact.save()


        #send mail
        send_mail(
             'Research Report Inquiry',
             'There has been inquiry for ' + listing + '. Sign into the admin panel for more info ',
             'godseye.research@gmail.com',
             ['ajaiswal646@gmail.com','godseye.research@gmail.com'],
             fail_silently=False

        )
        send_mail(
             'Research Report Inquiry Submitted',
             'We have received your query regarding ' + listing + '. We will get back to you soon! ',
             'godseye.research@gmail.com',
             [email],
             fail_silently=False

        )



        messages.success(
            request, 'Your request has been submitted, we will get back to you soon!')
        return redirect('/listings/'+listing_id)
