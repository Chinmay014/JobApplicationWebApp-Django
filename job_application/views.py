from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method =="POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print("I got here")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)
            Form.objects.create(first_name = first_name, last_name = last_name,
                                email=email,date=date,occupation=occupation)
            message_body = f"Thank you for your submission, {first_name}! Here are the details we received:\n"\
        f"your name: {first_name},\n last name: {last_name} \n date:{date}\n\n We will get in touch soon!"
            email_message = EmailMessage(subject="New Form Submission",body=message_body,to=[email])
            email_message.send()
            messages.success(request,"Form submitted successfully!")
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
