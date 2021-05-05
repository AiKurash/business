from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
    message_name = request.POST['message-name']
    message_email = reqeust.POST['message-email']
    message = request.POST['message']

    # Send Email
    send_mail(
        message_name,
        message,
        message_email,
        ['aikurashina@elysiancoder.com'],
        fail_silently=False,
    )
    return render(request, 'contact.html', {'message_name': message_name})

else:
    # return the page
    return render(request, 'contact.html', {})
