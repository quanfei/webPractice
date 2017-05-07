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
        #form = ContactForm(request.POST)
        #print("ok")
        #if form.is_valid():
         #   print("ok")
            form=request.POST
            name= form['Name']
            email = form['Email']
            subject = form['Subject']
            comment = form['Comment']

            recipients = ['edisonxmt@gmail.com']
            send_mail(
              subject,
              comment,
              'quanfeiwang@gmail.com',
              ['quanfeiwang@gmail.com'],
            )
           # send_mail(subject, comment, email, recipients)
    return render(
        request,
        'index.html',
    )