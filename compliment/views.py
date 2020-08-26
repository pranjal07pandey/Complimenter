from django.shortcuts import render
from django.contrib import messages
from twilio.rest import Client
client = Client("your sid", "your auth token")

# Create your views here.
def index(request):

    if request.method == 'POST':
            from_ = request.POST.get('from')
            to = request.POST.get('to')
            body = request.POST.get('body')

            msg = client.messages.create(
                to = to,
                from_ = from_,
                body = body
            )

            if msg:
                messages.success(request, "Compliment sent. Thank you!")
            else:
                messages.warning(request, "Something went wrong....")

    return render(request, 'compliment/index.html')