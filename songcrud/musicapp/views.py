from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, this is the music app")