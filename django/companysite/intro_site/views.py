from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

def contactinfo(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("ok")
        if form.is_valid():
            print("ok")
            name= form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            comment = form.cleaned_data['commet']

            recipients = ['edisonxmt@gmail.com']
            

            send_mail(subject, comment, email, recipients)
    return render(
        request,
        'index.html',
    )